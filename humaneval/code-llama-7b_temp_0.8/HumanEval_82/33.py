
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) in [2,3,5,7]:
        return True
    elif len(string) == 4 or len(string) % 2 == 0 or len(string) % 3 == 0 or len(string) % 5 == 0 or len(string) % 7 == 0:
        return False
    else:
        return True

