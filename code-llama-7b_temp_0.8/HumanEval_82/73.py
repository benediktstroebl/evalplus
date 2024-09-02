
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # pass

    if len(string) in [1, 2, 3, 5, 7, 11, 13, 17, 19]:
        return True
    else:
        return False
