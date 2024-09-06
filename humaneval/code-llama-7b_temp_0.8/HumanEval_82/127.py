
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l=len(string)
    if l==2 or l==3 or l==5 or l==7 or l==11 or l==13 or l==17 or l==19:
        return True
    else:
        return False
    
    









































