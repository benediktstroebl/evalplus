
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if string == '' or string =='':
        return False
    else:
        return len(string) in [2, 3] or all(string[i]!= string[i+1] for i in range(len(string)-1))




    
