
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your Code Here

    # PRIME_NUM = 1
    #
    # for p in string:
    #     p = ord(p)
    #     if p < PRIME_NUM:
    #         return False
    #     for i in range(2, p):
    #         if p % i == 0:
    #             return False
    # return True

    string_len = len(string)
    if string_len == 1:
        return False
    elif string_len == 2:
        return True
    else:
        return prime_length(string[1:])

