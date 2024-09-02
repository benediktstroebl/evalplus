
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    n = len(string)
    for i in range(2, n/2+1):
        if string[i:i+2] in string[0:i] or string[i:i+2] in string[i+1:n]:
            return False
    return True