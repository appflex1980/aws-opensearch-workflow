import os
import json
from opensearchpy import OpenSearch

# Read environment variables
OPENSEARCH_HOST = os.environ["OPENSEARCH_HOST"]
OS_USER = os.environ["OS_USER"]
OS_PASS = os.environ["OS_PASS"]

def lambda_handler(event, context):
    try:
        client = OpenSearch(
            hosts=[OPENSEARCH_HOST],
            http_auth=(OS_USER, OS_PASS),
            use_ssl=True,
            verify_certs=True,
            timeout=30
        )

        health = client.cluster.health()
        return {
            "statusCode": 200,
            "body": json.dumps(health)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
