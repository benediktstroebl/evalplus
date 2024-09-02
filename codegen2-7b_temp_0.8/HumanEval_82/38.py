
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if string!='string':
        return False
    else:
        string_length = len(string)
        if string_length < 2:
            return False
        if string_length == 2:
            return True
        else:
            return all(string[i] == string[i+1] for i in range(len(string)-
