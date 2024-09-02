
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    import math
    string = str(string)
    if len(string) == 1:
        return False
    for i in range(2, int(math.sqrt(len(string)))):
        if string[:i] * i == string:
            return False
    return True
