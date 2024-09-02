
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    s = set(string)
    if len(s) == 1:
        return True
    if len(s) == 2:
        if 'a' in s and 'b' in s:
            return True
        elif 'a' in s and 'o' in s:
            return True
        elif 'b' in s and 'o' in s:
            return True
        else:
            return False
    return False

