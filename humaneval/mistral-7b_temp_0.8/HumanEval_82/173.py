
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # init
    string_length = len(string)

    # logic
    if string_length < 2:
        return False

    if string_length == 2:
        return True

    for i in range(3, string_length + 1):
        if string_length % i == 0:
            return False

    return True

