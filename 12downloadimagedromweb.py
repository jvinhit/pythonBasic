import random
import urllib.request
def downloadimage(url):
    name = random.randrange(1,1000)
    full_name = str(name)+".jpg";
    urllib.request.urlretrieve(url,full_name)

downloadimage("https://scontent-hkg3-1.xx.fbcdn.net/v/t1.0-9/11949412_636761579798952_4694945758506347402_n.jpg?oh=9bad36a25d5cdc2fc6d8fbd1ad056597&oe=57B3B343")