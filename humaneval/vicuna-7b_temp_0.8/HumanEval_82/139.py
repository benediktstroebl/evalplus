
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check if the string is empty
    if len(string) == 0:
        return False
    
    # check if the string is a prime number
    for i in range(2, len(string)):
        if (string[0] == string[i] or string[0] == string[string.index(string[i])]) and string[i] == string[len(string) - 1]:
            return False
        
    return True
