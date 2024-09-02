
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
        return True
    return len(string) in [2,3] or all(string[i]!= string[i-1] and string[i]!= string[i+1] and string[i]!= string[i+2] and string[i]!= string[i-2] for i in range(1, len(string)-1))
