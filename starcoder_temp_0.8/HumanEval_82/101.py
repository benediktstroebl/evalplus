
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) < 1:
        return False
    elif len(string) == 1:
        return True
    elif len(string) == 2:
        if string[0] == string[1]:
            return False
        else:
            return True
    elif len(string) == 3:
        if string[0] == string[1] or string[0] == string[2] or string[1] == string[2]:
            return False
        else:
            return True
    else:
        for i in range(len(string)):
            for j in range(i, len(string)):
                if string[i]!= string[j]:
                    return False
    return True
