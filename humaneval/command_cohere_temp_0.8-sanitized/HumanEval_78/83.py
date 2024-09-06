import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    return sum(1 for x in re.findall('..?'+ '|'.join(primes), num))