from bs4 import BeautifulSoup
import requests
import random

s = requests.session()
url = s.get('http://www.babblenow.com')

values = {
    'username': input('Enter the Username: '),
    'password': input('Enter the Password: ')
}

result = s.post(
    'http://www.babblenow.com/helpers/index/authenticate_user.php',
    data= values
)

id = random.sample(range(11111111,99999999),20)
for key in id:
    values = {
        'text': 'Python is great , \'noob-to-pro\'',
        'postid': key
    }

    s.post(
        'http://www.babblenow.com/helpers/home/add_comment.php',
        data= values
    )

