
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    if len(string) > 1:
        for i in range(2, len(string)):
            if string[i] == '1':
                if (len(string) % (i+1) == 0) or (string[i] == '1' and (len(string) % (i+2) == 0)):
                    return False
            elif string[i] == '0':
                if len(string) % (i+1) == 0:
                    return False
        return True
    else:
        return False
