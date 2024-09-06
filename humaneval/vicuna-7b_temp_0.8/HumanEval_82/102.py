
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_count = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for num in prime_count:
        if string[0] == '3' or string[0] == '5' or string[0] == '7' or string[0] == '11':
            if string[-1] == num or string[-2] == num:
                return False
        if string[0] == num or string[-1] == num:
            return True
    return False
