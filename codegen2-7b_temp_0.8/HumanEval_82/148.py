
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if string.isalpha():
        return False
    elif len(string) <= 1:
        return False
    else:
        for i in range(2, int(len(string)/2)):
            if string[0:i].isalpha() is False:
                return True
        return False
    
