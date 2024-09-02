
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
    prime_numbers = [2,3,5,7,11,13,17,19]
    if length in prime_numbers:
        return True
    elif length % 2 == 0 or length % 3 == 0 or length % 5 == 0 or length % 7 == 0:
        return False
    else:
        return True

    
