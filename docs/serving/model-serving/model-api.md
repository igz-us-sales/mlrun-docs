# Model Server API

MLRun Serving follows the same REST API defined by Triton and [KFServing v2](https://github.com/kubeflow/kfserving/blob/master/docs/predict-api/v2/required_api.md)

Nuclio also support streaming protocols (Kafka, kinesis, MQTT, ..), in the case of streaming 
the `model` name and `operation` can be encoded inside the message body

## get server info

    GET /
    GET /v2/health

response example: `{'name': 'my-server', 'version': 'v2', 'extensions': []}`

## list models

    GET /v2/models/

response example:  `{"models": ["m1", "m2", "m3:v1", "m3:v2"]}`

## get model metadata

    GET v2/models/${MODEL_NAME}[/versions/${VERSION}]

response example: `{"name": "m3", "version": "v2", "inputs": [..], "outputs": [..]}`

## get model health / readiness

    GET v2/models/${MODEL_NAME}[/versions/${VERSION}]/ready

returns 200 for Ok, 40X for not ready.

## infer / predict

    POST /v2/models/<model>[/versions/{VERSION}]/infer

request body:

    {
      "id" : $string #optional,
      "model" : $string #optional
      "data_url" : $string #optional
      "parameters" : $parameters #optional,
      "inputs" : [ $request_input, ... ],
      "outputs" : [ $request_output, ... ] #optional
    }

- **id:** unique Id of the request, if not provided a random value will be provided
- **model:** model to select (for streaming protocols without URLs)
- **data_url:** option to load the `inputs` from an external file/s3/v3io/.. object
- **parameters:** optional request parameters
- **inputs:** list of input elements (numeric values, arrays, or dicts)
- **outputs:** optional, requested output values 

> Note: you can also send binary data to the function, for example a JPEG image, the serving engine pre-processor 
will detect that based on the HTTP content-type and convert it to the above request structure, placing the 
image bytes array in the `inputs` field.

response structure:

    {
      "model_name" : $string,
      "model_version" : $string #optional,
      "id" : $string,
      "outputs" : [ $response_output, ... ]
    }

## explain

POST /v2/models/<model>[/versions/{VERSION}]/explain

request body:

    {
      "id" : $string #optional,
      "model" : $string #optional
      "parameters" : $parameters #optional,
      "inputs" : [ $request_input, ... ],
      "outputs" : [ $request_output, ... ] #optional
    }

response structure:

    {
      "model_name" : $string,
      "model_version" : $string #optional,
      "id" : $string,
      "outputs" : [ $response_output, ... ]
    }


