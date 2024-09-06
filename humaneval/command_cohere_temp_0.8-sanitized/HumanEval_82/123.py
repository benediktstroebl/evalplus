def is_prime_length(length):
    """
    Returns True if the provided length is prime, False otherwise.
    """
    if length <= 1:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    """
    if len(string) == 0:
        return False
    return is_prime_length(len(string))