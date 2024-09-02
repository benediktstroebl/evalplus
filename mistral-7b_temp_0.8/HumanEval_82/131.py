
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check that the length is an integer
    if not isinstance(string, str):
        raise ValueError("'string' should be of string type")
    # use .len() to get the string length
    length = len(string)
    # check if the length is 0
    if length == 0:
        return False
    # check if the length is 1
    elif length == 1:
        return True
    # check if the length is 2
    elif length == 2:
        return True
    # check if the length is 3
    elif length == 3:
        return True
    # check if the length is divisible by 2
    elif length % 2 == 0:
        return False
    # check if the length is divisible by 3
    elif length % 3 == 0:
        return False
    # check if the length is divisible by 5
    elif length % 5 == 0:
        return False
    # check if the length is divisible by 7
    elif length % 7 == 0:
        return False
    #
