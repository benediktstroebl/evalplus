
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # MY ANSWER:
    # prime_length = len(string)
    # if prime_length == 2 or prime_length == 3 or prime_length == 5 or prime_length == 7 or prime_length == 11 or prime_length == 13 or prime_length == 17 or prime_length == 19:
    #     return True
    # else:
    #     return False
    #
    # MY FRIEND'S ANSWER:
    if len(string) == 2 or len(string) == 3 or len(string) == 5 or len(string) == 7 or len(string) == 11 or len(string) == 13 or len(string) == 17 or len(string) == 19:
        return True
    else:
        return False

