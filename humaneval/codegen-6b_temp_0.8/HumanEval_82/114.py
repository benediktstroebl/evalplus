
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    if len(string) == 2:
        return True
    if len(string) % 2 == 0:
        return False
    half = len(string) / 2
    for i in range(3, half + 1, 2):
        if string[:i] * int(string[:i]) == string:
            return False
    return True

