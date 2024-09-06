import math
def is_prime(n):
    """
    Checks if a number is a prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    counter = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    # Remove all non-hexadecimal digits and convert to lowercase
    cleaned_num = ['0123456789ABCDEFabcdef'.index(c) for c in num if c in digits and c.isupper()]
    cleaned_num = ['%sx' % cleaned_num[0]] + cleaned_num[1:]; cleaned_num = list(map(int, cleaned_num))
    
    while cleaned_num:
        if is_prime(cleaned_num[0]):
            counter += 1
        cleaned_num = cleaned_num[1:]
    return counter