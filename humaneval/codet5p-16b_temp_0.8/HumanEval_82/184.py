
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    for i in range(len(string)):
        if len(string[:i+1]) >= 2:
            if prime_length(string[:i+1]) == True:
                return True
    return False
