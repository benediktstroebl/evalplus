import math
def is_prime(n):
    """
    Checks if a number is a prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    # your code here
    digit_primes = 0
    num = str(num)
    # assuming the input is always correct or empty string
    # removing A-F to convert hexadecimal to decimal
    num = num.replace("A","").replace("B","").replace("C","").replace("D","").replace("E","").replace("F","")
    for char in num:
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # char is A, B, C, D, E or F, decimal is 11, 13, 17, 19, 1A, 1B, 1C, 1D, 1E, 1F
            if is_prime(int(char)):
                digit_primes += 1
        elif is_prime(int(char)):
            digit_primes += 1
    return digit_primes