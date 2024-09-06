
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    s = set(string)
    s = len(s)
    x= 0
    for i in range (1,s):
        if s%i == 0:
            x +=1
    if x==2:
        return True
    else:
        return False

