
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

    return all(map(lambda x: len(x) % 2 == 0, [string[i:i + 2] for i in xrange(len(string) - 1)]))
