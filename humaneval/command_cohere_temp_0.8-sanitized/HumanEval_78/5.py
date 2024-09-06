import math
def is_prime(n):
    """
    Checks if a number is prime
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
    # remove non-hexadecimal digits and convert to uppercase
    cleaned_num = ""
    for char in num:
        if char in "0123456789ABCDEF":
            cleaned_char = char.upper()
        else:
            cleaned_char = "0"
        cleaned_num += cleaned_char
        
    count = 0
    for digit in cleaned_num:
        if is_prime(int(digit)):
            count += 1
    return count