
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # first check if the string length is 0
    if len(string) == 0:
        return True
    # then check if the string length is greater than 1
    if len(string) > 1:
        # then check if the string is in the prime list
        for i in range(2, len(string)+1):
            if len(string) % i == 0:
                return False
        else:
            return True
    # if not, return False
    else:
        return False
