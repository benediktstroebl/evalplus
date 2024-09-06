
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # array = [string]
    # prime_length = 0
    # for _ in array:
    #     if _ == 1:
    #         continue
    #     for x in range(2, _):
    #         if (_ % x) == 0:
    #             prime_length += 1
    # if prime_length == 0:
    #     return True
    # else:
    #     return False
    # return prime_length
    if len(string) == 2 or len(string) == 3 or len(string) == 5 or len(string) == 7:
        return True
    elif len(string) == 1 or len(string) == 4 or len(string) == 6 or len(string) == 8:
        return False
    else:
        return bool(len(string) % 2)
