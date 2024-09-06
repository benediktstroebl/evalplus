import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0
    num = re.sub('[^A-Fa-f0-9]','',num)
    if(num==''):
        return 0
    for digit in num:
        if digit in hex_digits:
            if digit in primes:
                count += 1
        elif digit==' ':
            continue
        else:
            return -1
    return count