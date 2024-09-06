import math
def is_prime(n):
    """Check if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # your code here
    count = 0
    num = str(num)
    # Assuming the input is always correct or empty string
    # removing 'A', 'B', ... 'F' from the string and converting 
    # to integer to work with built-in is_prime function
    for char in list(num):
        if char.isupper() and char in 'ABCDEF':
            num = num.replace(char, str(int(char) - ord('A') + 10))
    for digit in str(num):
        if is_prime(int(digit)):
            count += 1
    return count