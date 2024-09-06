
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if string.isdigit() == False:
        return False
    for i in range(1, len(string)):
        if string[i:].isdigit() == True and string[i:i+2] == string[i:i+2].isdigit():
            if str(int(string[:i+1]) * 10 + int(string[i+1])) == str(int(string[:i] * 10 + int(string[i+2])) % 10):
                return False
        if string[i:].isalpha() == True:
            if len(string) % 2 == 0:
                return False
        if string.isdigit() == True:
            if string[i:].isdigit() == True and string[i:i+2] == string[i:i+2].isdigit():
                if str(int(string[:i+1]) * 10 + int(string[i+1])) == str(int(string[:i] * 10 + int(string[i+2])) % 10):
                    return False
        if string[i:].isalpha() == True:
            if len(string) % 2 == 0:
                return False
    return True
