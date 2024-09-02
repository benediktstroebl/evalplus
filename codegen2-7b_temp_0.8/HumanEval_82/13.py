
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    try:
        if int(string) < 2:
            return False
        if int(string) == 2:
            return True
        for i in range(2, int(string)):
            if string % i == 0:
                return False
        return True
    except:
        return
