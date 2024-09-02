
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    length = len(string)
    if length <= 1 or string == 'a':
        return False
    elif len(set(string)) == 1:
        return True
    else:
        for i in range(2, length):
            if length % i == 0:
                return False
        return True
