
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string_len = len(string)
    if string_len == 2:
        return True
    for i in range(3, string_len + 1):
        if string_len % i == 0:
            return False
    return True

