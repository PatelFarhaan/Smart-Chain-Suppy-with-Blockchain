import json
import boto3
from botocore.exceptions import ClientError


def email_sending_logic(company_name):
    RECIPIENT = ["patel.farhaaan@gmail.com"]
    AWS_REGION = "us-east-1"
    SENDER = "blockchain.cmpe281@gmail.com"
    SUBJECT = "BLOCKCHAIN ALERT"
    # BODY_TEXT = ("Hello TEAM,"
    #              f"The API was not able to find the following company's logo : {company_name}."
    #              "By Team,"
    #              "ANGELFUND AI"
    #              )
    BODY_HTML = '''
  <html lang="en" dir="ltr">
    <head>
      <meta charset="utf-8">
      <title>BlockChain</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
          integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
          crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
          integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
          crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
          integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
          crossorigin="anonymous"></script>
    </head>
    <body>
      <br>
      <br>
      <div class="container">
          <div class="jumbotron">
            <h1 align="center">BlockChain Tampered</h1>
          </div>
          <br>
          <div class="jumbotron">
            <h4>Hello {0},</h4>
            <h4>The Blockchain with the ID {1} has been tampered.</h4>
            <br>
            <h4>By Team,</h4>
            <h4>Blockchain</h4>
          </div>
          <br>
          <br>
          <br>
      </div>
    </body>
  </html>
            '''.format(user_name, company_name)
    CHARSET = "UTF-8"
    client = boto3.client('ses',
                          region_name=AWS_REGION,
                          aws_access_key_id=' AKIASTBAW2HGI2FFCZXU',
                          aws_secret_access_key='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'
                          )
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': RECIPIENT,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    # 'Text': {
                    #     'Charset': CHARSET,
                    #     'Data': BODY_TEXT,
                    # },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    else:
        print("Email sent! Message ID:", response['MessageId'])
        return True


def lambda_handler(event, context):
    input_body = json.loads(event['body'])
    company_name = input_body['company_name']
    user_name = input_body['user_name']

    resp = email_sending_logic(user_name, company_name)
    return_obj = { "result": resp}
    return_result = { "body": json.dumps(return_obj) }
    return return_result


