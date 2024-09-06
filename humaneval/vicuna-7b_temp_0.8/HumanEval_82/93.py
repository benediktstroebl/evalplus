
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check if the string is empty
    if len(string) == 0:
        return True

    # check if the string is only one character
    if len(string) == 1:
        return False

    # check if the string is a prime number
    for i in range(2, len(string)):
        if (string[i] - (i % 2)) % 2 != 0:
            return True

    return False
