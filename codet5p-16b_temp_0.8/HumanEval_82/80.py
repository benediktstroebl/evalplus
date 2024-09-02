
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    str_len = len(string)
    if str_len == 1:
        return False
    elif str_len == 2:
        return True
    else:
        if str_len % 2 == 0:
            return False
        else:
            for i in range(3, str_len, 2):
                if str_len % i == 0:
                    return False
            return True

