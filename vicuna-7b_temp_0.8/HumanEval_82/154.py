
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    divisor = 2
    for i in range(2,len(string)):
        if(string[i] == string[i-1] * 2 or string[i] == string[i-1] + string[i-2] % 2):
            return False
        if(string[i] % 2 == 0):
            return False
        divisor = divisor + 1
    return True
