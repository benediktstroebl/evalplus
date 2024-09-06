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
    counter = 0
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    
    # Iterate each digit in the input string
    for digit in num:
        # Convert the digit to a decimal number
        digit_decimal = int(digits.index(digit))

        # Check if the digit is prime
        if is_prime(digit_decimal):
            counter += 1

    return counter