
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if (len(string) < 2):
        return False
    else:
        for i in range(len(string)):
            if (string[i] == string[len(string)-1]):
                return False
        else:
            return True
