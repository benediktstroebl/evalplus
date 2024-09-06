
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    a=len(string)
    if a==1:
        return True
    if a==2:
        return True
    for i in range(3, a+1, 2):
        if a%i==0:
            return False
    return True
