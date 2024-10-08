def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isalpha() and digit.upper() in primes:
            count += 1
        elif digit.isdigit() and int(digit) in [1, 7]:
            count += 1
    return count
