
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if string[0] in '0123456789':
        return False

    for number in range(2, int(string)):
        if int(string) % number == 0:
            return False
        else:
            pass
    return True

