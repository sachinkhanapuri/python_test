import requests
import json
from urllib.request import urlopen
#json_url=urlopen("https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=439d4b804bc8187953eb36d2a8c26a02")
json_url=urlopen("https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=439d4b804bc8187953eb36d2a8c26a02")

response=json_url.read()
data=json.loads(response)
#print(data)
#print(type(data))
for keys,values in data.items():
    #print('keys:',keys)
    #print('values:',values)
    if keys =='dt':

        if values > 1:
        # check for factors
            for i in range(2, values):
                if (values % i) == 0:
                    print(values, "is not a prime number")
                    print(i, "times", values // i, "is", values)
                    break
                else:
                    print(values, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
        else:
            print(values, "is not a prime number")


