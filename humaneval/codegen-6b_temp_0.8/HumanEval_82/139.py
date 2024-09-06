
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        for i in range(0, len(string)):
            if isprime(i) and isprime(len(string) - i):
                return True
    return False
