import requests

headers = {
    'Host': 'spada.kemdikbud.go.id',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('ses', '4Iaso52mVXPdT5yUWnJPamZsU1lbrKacn6TEoMdacVqfqJ+m182bcKuoqJ3Hm6ejZq2bl52nX46cZZybT2KFmcuqqqyglKKWh55ZYmlkaWmTXmxha2heZWlZXU+lmKarm5fQmIRyWX6XlaeaxtJXcaqYnFmyjqGXnauhqFZjU5KmmJyjT3CFlMaloKZyoKqb2tZlmZxWX1vOkqmVpK2gmKZZa2C2Y1WtT3CFZpBwZWpdU11z2s2jlHJUZWmUXWNkamxWVWBZoY6tn1VxT57Xp9KrcZRhj2Sc2tCmnmpiqKfGlqNemZtbnJhZXU+pqZidlq6FbYSjo6Zkkleu'),
)
n=0
while (1):
    response = requests.get('https://spada.kemdikbud.go.id/spada-identiti', headers=headers, params=params, verify=False)
    print(response.status_code, n)
    n += 1
