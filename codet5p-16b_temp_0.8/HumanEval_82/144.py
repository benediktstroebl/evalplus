
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if string == '':
        return False
    length = len(string)
    if length == 1:
        return True
    if length == 2:
        return string[0] == string[1]
    for i in range(2, length):
        if string[i] == string[0] and string[i] == string[1]:
            return False
    return True
