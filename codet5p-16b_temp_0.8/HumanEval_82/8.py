
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    
    if len(string) == 2:
        return len(string) == 2
    elif len(string) == 3:
        return len(string) == 3
    else:
        for i in range(2,len(string)):
            if len(string) % i == 0:
                return False
            elif i == len(string):
                return True

