
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    str_length = len(string)
    if str_length > 1:
        for i in range(2,str_length):
            if (str_length % i) == 0:
                return False
        return True
    else:
        return False
