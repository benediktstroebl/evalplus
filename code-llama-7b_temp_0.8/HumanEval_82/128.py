
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if (len(string) == 1) or (len(string) == 3):
        return True
    elif len(string) == 2 or len(string) == 4 or len(string) == 6 or len(string) == 5:
        return False
    else:
        return prime_length(string[1:])
