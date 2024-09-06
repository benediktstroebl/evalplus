
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # SOLUTION
    # prime numbers are >= 1
    # so if the length of the string is a prime number
    # the function will return True
    
    length = len(string)
    for i in range(2, length):
        if (length % i == 0):
            return False
        else:
            return True
        
        
        
            
