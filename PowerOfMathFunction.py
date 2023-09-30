# import the JSON utility packages
import json
# import the power math library
import math

# define the handler function that the lambda service will use an entry point.
def lambda_handler(event, context):
    mathResult = math.pow(int(event['base']), int(event['exponent']))

    # return properly formatted Json Obejct
    return {
        'statusCode': 200,
        'body': json.dumps('Yout result is ' + str(mathResult))
    }