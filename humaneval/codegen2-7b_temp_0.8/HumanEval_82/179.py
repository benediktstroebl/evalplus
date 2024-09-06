
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if string[0] == 'a':
        return True
    else:
        for i in range(len(string)):
            if string[i] == 'a':
                return True
            elif string[i] == 'e':
                return True
            elif string[i] == 'i':
                return True
            elif string[i] == 'o':
                
