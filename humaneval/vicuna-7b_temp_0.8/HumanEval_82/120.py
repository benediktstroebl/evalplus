
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string is empty
    if len(string) == 0:
        return False
    
    # Check if the string is a prime number
    for i in range(2, int(len(string)**0.5) + 1):
        if string[0] == '2' or string[0] == '3' or string[0] == '5' or string[0] == '7' or string[0] == '11':
            if string[0] == '2' and string[1] == '2':
                continue
            if string[0] != str(i) and str(i) != string[0]:
                return False
        if string[0] == str(i) or str(i) == string[0]:
            continue
        if string[0:i] == string[i:] + '1':
            continue
        if len(string) % i == 0:
            return False
    return True
