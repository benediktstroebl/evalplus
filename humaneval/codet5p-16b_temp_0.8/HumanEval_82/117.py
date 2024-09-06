
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    for i in range(2,int(string[-1])+1):
        if int(string[-1]) % i == 0 and int(string[-1]) > 1:
            return False
        else:
            return True

    return True

