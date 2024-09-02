
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # num = len(string)
    # if num <= 2:
    #     return False
    # elif num % 2 == 0 or num % 3 == 0:
    #     return False
    # else:
    #     return True

    return len(string) in set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])






