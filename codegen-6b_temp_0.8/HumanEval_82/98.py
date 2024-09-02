
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) < 2:
        return True

    # first we make sure that the number is not divisible by any other
    # number before performing a test
    for i in range(2, int(len(string))):
        if (string[:i] * (len(string)//i)) == string:
            return False

    return True
