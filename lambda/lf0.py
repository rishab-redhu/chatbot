import json

def lambda_handler(event, context):
    
    reply = {"messages": list()}
    for botrequest in event["messages"]:
        mytextextresponse = "Application under development. Search functionality will be implemented in Assignment 2"
        myresponse = {
            "type": botrequest["type"],
            "unstructured": {
                "id": botrequest["unstructured"]["id"],
                "text": mytextextresponse,
                "timestamp": botrequest["unstructured"]["timestamp"]
            }
        }
        reply["messages"].append(myresponse)
        
    return reply
