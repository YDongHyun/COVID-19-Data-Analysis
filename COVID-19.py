from urllib.parse import urlencode, unquote,quote_plus
from urllib.request import urlopen
import urllib

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'phB%2B74RS9Cmx6xXwRsbWm%2B8%2BIGJyF%2F0ULtA%2FuV8VVZNpGbQN8xOO3bfscWaCA9dZc3HyWEevnxmImf%2Fqt3JSbA%3D%3D',
                                quote_plus('pageNo') : '1',
                                quote_plus('numOfRows') : '10',
                                quote_plus('startCreateDt') : '20200310',
                                quote_plus('endCreateDt') : '20200315' })

request = urllib.request.Request(url + unquote(queryParams))
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)
