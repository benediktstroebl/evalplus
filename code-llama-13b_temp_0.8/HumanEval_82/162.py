
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # check if string is empty or not a string
    if not string or not isinstance(string, str):
        return False

    # if string is 1 or negative, then return False
    if len(string) == 1 or len(string) < 0:
        return False

    # check if string length is prime
    if len(string) == 2 or len(string) == 3 or len(string) == 5:
        return True
    elif len(string) < 2:
        return False
    else:
        for i in range(2, len(string)):
            if len(string) % i == 0:
                return False
        else:
            return True
