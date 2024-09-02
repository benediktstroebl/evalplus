
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    #string_len = len(string)
    #if string_len == 2 or string_len == 3 or string_len == 5 or string_len == 7:
    #    return True
    #elif string_len % 2 == 0 or string_len % 3 == 0 or string_len % 5 == 0 or string_len % 7 == 0:
    #    return False
    #else:
    #    return True
    return True if len(string) in [2,3,5,7] else len(string) % 2 == 0 or len(string) % 3 == 0 or len(string) % 5 == 0 or len(string) % 7 == 0

