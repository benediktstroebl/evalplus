
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
    if length % 2 == 0:
        length = length / 2
    else:
        length = (length - 1) / 2
    if length == 1:
        return True
    return False
