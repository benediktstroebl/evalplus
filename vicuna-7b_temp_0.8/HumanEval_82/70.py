
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check for empty string
    if not string:
        return True

    # check if the string is a prime number
    if len(string) > 1:
        for i in range(2, len(string)):
            if string[i] == '1' or string[i] == '3' or string[i] == '7' or string[i] == '9':
                if string[0] == string[i] - 1 or string[0] == string[i] + 1 or \
                   string[0] == string[i] * 10 or string[0] == string[i] * 3 - 1 or \
                   string[0] == string[i] * 3 + 1:
                    return False
                else:
                    return True
    return True