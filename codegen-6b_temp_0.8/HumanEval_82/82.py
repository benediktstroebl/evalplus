
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # if the length is 1 or 0, or 1 letter is in the string, it is not a prime
    # number.
    # if the length is 2, then only the letters that are unique are in the
    # string.
    # if there is nothing but letters in the string, it is a prime number.
    letters = set(string)
    if len(letters) == 0 or len(letters) == 1:
        return True
    elif len(letters) == 2:
        return False
    else:
        return True

