
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    # Make sure the length is an integer
    if type(l) is not int:
        return False
    # If the length is 0 or less, return False
    if l < 1:
        return False
    # If the length is 1 or 2, return True
    if l == 1 or l == 2:
        return True
    # If the length is even, return False
    if l % 2 == 0:
        return False
    # If the length is odd, check if any of the factors are prime
    for i in range(2, l+1):
        if l % i == 0:
            return False
    return True
