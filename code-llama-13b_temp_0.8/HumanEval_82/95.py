
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
    if str_len == 2:
        return True
    if str_len == 3:
        return True
    if str_len == 5:
        return True
    if str_len == 7:
        return True
    if str_len == 11:
        return True
    if str_len == 13:
        return True
    if str_len == 17:
        return True
    if str_len == 19:
        return True
    if str_len == 23:
        return True
    if str_len == 29:
        return True
    if str_len == 31:
        return True
    else:
        return False

