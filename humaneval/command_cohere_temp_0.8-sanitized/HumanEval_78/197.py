import math
def hex_key(num):
    prime_hex = [1 for i in range(0,16)]
    p = 2
    while p * p <= hex_digit_max: 
        is_prime = True
        for i in range(0,16):
            if (p * hex_digit_to_int[i] <= hex_digit_max and 
                prime_hex[i] == 0):
                is_prime = False
                break
        if is_prime:
            for i in range(0,16):
                if (p * hex_digit_to_int[i] <= hex_digit_max and 
                    prime_hex[i] == 1):
                    prime_hex[i] = 0
        p += 1
    #print(prime_hex)
    count = 0
    for digit in num:
        if prime_hex[int(digit)] == 1:
            count += 1
    return count
def hex_digit_to_int(digit):
    if digit >= 'A' and digit <= 'F':
        return int(digit) - 9 
    elif digit >= 'a' and digit <= 'f':
        return int(digit) - 9 
    elif digit >= '0' and digit <= '9':
        return int(digit) 
    else:
        return 0
hex_digit_max = int('F' + '0', 16)