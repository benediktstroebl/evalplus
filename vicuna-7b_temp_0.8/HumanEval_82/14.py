
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string = list(string)
    for i in range(2, len(string)):
        if (string[i] == '1' and string[i-1] != '1'):
            for j in range(i+1, len(string)):
                if (string[j] == '1' and string[j-1] != '1'):
                    return False
        elif (string[i] == '1' and string[i-2] != '1'):
            for j in range(i+1, len(string)):
                if (string[j] == '1' and string[j-1] != '1'):
                    return False
        elif (string[i] != '1' and string[i-1] == '1'):
            for j in range(i+1, len(string)):
                if (string[j] == '1' and string[j-1] != '1'):
                    return False
        else:
            return True
    return False