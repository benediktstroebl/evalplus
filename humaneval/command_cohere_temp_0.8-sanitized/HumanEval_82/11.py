def is_prime_length(length):
    """
    Returns True if the inputted number is a prime number, else False.
    Args:
        length (int): The length of the input string to be checked if its length is a prime number
    Returns:
        bool
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
    return is_prime_length(len(string))