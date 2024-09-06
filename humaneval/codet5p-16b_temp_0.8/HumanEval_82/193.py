
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if len(string) < 2:
        return True
    if len(string) == 2 and string[0] == string[1]:
        return True
    if len(string) == 2 and string[0]!= string[1]:
        return False
    if string[0]!= string[1] and string[1] == string[2]:
        return True
    else:
        return False
