![Python](https://img.shields.io/badge/Python-3.6-blue.svg) [![GitHub license](https://img.shields.io/github/license/serhattsnmz/Tardigrade.svg)](https://github.com/serhattsnmz/Tardigrade/blob/master/LICENSE) [![](https://images.microbadger.com/badges/image/xshuden/tardigrade.svg)](https://microbadger.com/images/xshuden/tardigrade "Get your own image badge on microbadger.com") [![](https://images.microbadger.com/badges/version/xshuden/tardigrade.svg)](https://microbadger.com/images/xshuden/tardigrade "Get your own version badge on microbadger.com")

## Tardigrade (Subdomian Finder)

- Python script for url crawling and subdomain finding. 

## Requirements

- Python 3.6+
- Requests
- Prettytable

## How to install and run

1. Download the source from Github
    - `git clone https://github.com/serhattsnmz/Tardigrade.git`
    - `cd Tardigrade`
2. Install requirements
	- `pip install -r requirements.txt`
3. Run python file with Python 3
	- `python3 tardigrade.py`

## Docker Run Command

```
docker run --rm -it -e "DOMAIN=<**SITE URL**>" -e "VERBOSE=<**True/False**>" -e "SAVEFILE=<**True/False**>" xshuden/tardigrade # container is deleted when you're done
OR
docker run -it -e "DOMAIN=<**SITE URL**>" -e "VERBOSE=<**True/False**>" -e "SAVEFILE=<**True/False**>" xshuden/tardigrade
```

## Docker Example Command
```
docker run --rm -it -e "DOMAIN=google.com" -e "VERBOSE=True" -e "SAVEFILE=True" xshuden/tardigrade
docker run -it -e "DOMAIN=google.com" -e "VERBOSE=True" -e "SAVEFILE=True" xshuden/tardigrade
```

## Usage

Simply call `python tartigrade.py`

Domain and subdomain list to ask you to make a discovery.

You must create the subdomain file yourself.

You will have:
- You will learn about other sites within the website
- Explore subdomain addresses of sites
- You will learn the IP addresses of sites with subdomains.

## Advanced Usage

```
usage: tardigrade.py [-h] -d  -t  [-v] [-s]

Fetch all the lectures for a Instagram

Fetch and try all the links in a url address.

optional arguments:
  -h, --help        show this help message and exit
  -d , --domain     Domain name
  -t , --text       Subdomain file
  -v , --verbose    See the results in real time
  -s , --savefile   Save result to json file
```

## Example

```
$ python3 tardigrade.py -d github.com -t subdomain.txt
```

Output:
```
+-------------------------------+-----------------+
|          Domain Name          |    IP Address   |
+-------------------------------+-----------------+
|     http://www.twitter.com    |   104.244.42.1  |
|    http://mail.twitter.com    |  216.58.206.164 |
|      http://m.twitter.com     |  104.244.42.134 |
|    http://www.linkedin.com    |   185.63.144.1  |
|     http://m.linkedin.com     |   185.63.144.1  |
|       http://www.w3.org       |  128.30.52.100  |
|    http://www.amazonaws.com   |   52.46.129.40  |
|     http://www.GitHub.com     |  192.30.253.113 |
|      http://db.GitHub.com     | 185.199.110.153 |
|     http://www.youtube.com    |  216.58.212.46  |
|      http://m.youtube.com     |  216.58.212.46  |
|     http://www.example.com    |  93.184.216.34  |
|     http://www.github.com     |  192.30.253.113 |
|      http://db.github.com     | 185.199.109.153 |
| http://www.githubuniverse.com | 185.199.109.153 |
|    http://www.facebook.com    |   31.13.84.36   |
|     http://m.facebook.com     |   31.13.84.36   |
+-------------------------------+-----------------+

```
