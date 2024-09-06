import math
def hex_key(num):
    """
    Determine the number of hexadecimal digits that are primes.
    """
    
    # Use the math library's prime checking function
    # to check if each digit is prime or not
    return sum(1 for digit in num if math.prime(int(digit, 16)))