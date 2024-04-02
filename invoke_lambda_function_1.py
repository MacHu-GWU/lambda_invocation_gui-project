# -*- coding: utf-8 -*-

import os
import json

import boto3

param1 = os.environ["PARAM1"]
param2 = os.environ["PARAM2"]

print("Invoke Lambda Function with the following parameters:")
print(f"{param1 = }")
print(f"{param2 = }")


def main():
    lbd_client = boto3.client("lambda")
    # ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/client/invoke.html
    payload = {
        "param1": param1,
        "param2": param2,
    }
    res = lbd_client.invoke(
        FunctionName="your_lambda_function_name",
        InvocationType="RequestResponse",
        LogType="Tail",
        Payload=json.dumps(payload),
    )
    print("--- log ---")
    log = res["LogResult"]
    print(log)
    print("--- output ---")
    output = res["Payload"].read().decode("utf-8")
    print(output)


# if __name__ == "__main__":
#     main()
