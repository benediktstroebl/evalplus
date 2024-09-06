
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    prime_length = len(string)
    count = 0
    for x in range(1, prime_length + 1):
        if prime_length % x == 0:
            count += 1
        if count > 2:
            return False
    return True
    
