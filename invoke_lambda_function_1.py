# -*- coding: utf-8 -*-

import os
import boto3

param1 = os.environ["PARAM1"]
param2 = os.environ["PARAM2"]

print("Invoke Lambda Function with the following parameters:")
print(f"{param1 = }")
print(f"{param2 = }")
