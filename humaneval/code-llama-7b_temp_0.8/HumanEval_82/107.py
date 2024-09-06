
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime = 0
    for n in range(1, len(string)):
        if (len(string) % n) == 0:
            prime = prime + 1
        else:
            pass
    if prime == 0:
        return True
    else:
        return False

