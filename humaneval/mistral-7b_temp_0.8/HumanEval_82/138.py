
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Only change code below this line
    s=len(string)
    if s==1:
        return True
    for i in range(2,s//2+1):
        if s%i==0:
            return False
    return True
