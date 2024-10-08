
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
    if str_len < 2:
        return False

    for i in range(2, str_len):
        if str_len % i == 0:
            return False

    return True

