
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # inefficient solution, but good enough for this exercise
    num_digits = len(string)
    for i in range(2, num_digits):
        if string[0] == '1' or string[0] == '3' or string[0] == '7':
            if string[1:] % i == 0:
                return False
        if string[0] == '2':
            if string[1:] % (i+1) == 0:
                return False
    return True
