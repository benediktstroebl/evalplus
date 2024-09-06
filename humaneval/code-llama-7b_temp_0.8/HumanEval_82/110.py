
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
    if str_len == 0 or str_len == 1:
        return False
    elif str_len == 2:
        return True
    else:
        for prime in range(3, int(str_len / 2) + 1, 2):
            if str_len % prime == 0:
                return False
            else:
                return True
