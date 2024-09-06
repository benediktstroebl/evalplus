
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    string = string.lower()
    length = len(string)
    if length == 1:
        return True
    if length == 2:
        return True if string.isalpha() else False
    if length % 2 == 0:
        return False
    for i in range(3, int(length/2), 2):
        if length % i == 0:
            return False
    else:
        return True
        
