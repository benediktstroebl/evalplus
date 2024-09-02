
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l_string = len(string)
    if l_string <= 1:
        return False
    for i in range(2, l_string//2 + 1):
        if l_string % i == 0:
            return False
    return True

