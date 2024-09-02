
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if (len(string) == 0):
        return False
    elif (len(string) == 1):
        return False
    else:
        for i in string:
            if (i == '1' or i == '3' or i == '7' or i == '9'):
                continue
            else:
                return False
