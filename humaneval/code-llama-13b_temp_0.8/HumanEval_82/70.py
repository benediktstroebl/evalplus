
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    if string in prime_list:
        return True
    elif len(string) > 31:
        return False
    else:
        return False
