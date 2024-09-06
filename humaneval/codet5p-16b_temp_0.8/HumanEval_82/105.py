
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if len(string) == 1:
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    else:
        for i in range(2,len(string)-1):
            if string[i] == string[0] or string[i] == string[-1]:
                return False
        return True
            
        
