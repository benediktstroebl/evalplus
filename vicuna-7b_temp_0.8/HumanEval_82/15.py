
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
    
    # check if the string is a digit
    if not string.isdigit():
        return False
    
    # check if the string is '1'
    if string.lower() == '1':
        return True
    
    # check if the string is prime
    for i in range(2, int(string**0.5) + 1):
        if string[0] == '1' or string[0] == string[i]:
            continue
        for j in range(1, len(string)):
            if (i * j) % string == 0:
                return False
        return True
    return False
