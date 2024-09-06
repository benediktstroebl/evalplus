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
    counter = 0
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    if num == "":
        return 0

    for digit in digits:
        if digit in num:
            index = num.find(digit)
            if index == -1:
                return 0
            num = num[index + 1:]
            if len(num) == 0:
                return 0
            if is_prime(int(digit, 16)):
                counter += 1

    return counter