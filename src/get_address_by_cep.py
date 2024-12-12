import json
import urllib
import re

def lambda_handler(event, context):

    if 'cep' in event and _regex(event['cep']):
        return json.loads(urllib.request.urlopen(_get_url_api(event['cep'])).read())
    return json.loads("{\"erro\": true, \"mensagem\": \"Formato incorreto\"}")

def _get_url_api(cep):
    return ('http://www.viacep.com.br/ws/{}/json'.format(_replace(cep)))
    
def _replace(str):
    return str.replace("-", "").replace(" ", "")
    
def _regex(str):
    return re.match('[0-9]{8}', _replace(str))