
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
    if l == 1:
        return True
    if l == 2:
        return True
    i = 2
    while i * i <= l:
        if l % i == 0:
            return False
        i += 1
    return True

