
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime = []
    for i in xrange(len(string)):
        if string[i] in prime:
            return False
        else:
            prime.append(string[i])
    return True
