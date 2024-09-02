
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # c = 0
    # for i in string:
    #     if i == ' ':
    #         c += 1
    # if c > 1:
    #     return False
    # elif c + 1 == len(string):
    #     return True
    # else:
    #     return False

    # solution 2
    if isinstance(string, str):
        for i in range(2, len(string)):
            if not string.startswith(' ') and i == len(string) - i:
                return True
            elif string.startswith(' ') or string.startswith('-'):
                return False
        return True

