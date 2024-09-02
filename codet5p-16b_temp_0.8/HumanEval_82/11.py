
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    length = len(string)
    if length == 2:
        return True
    else:
        if length % 2 == 0:
            return False
        else:
            for x in range(3, length):
                if length % x == 0:
                    return False
            return True
