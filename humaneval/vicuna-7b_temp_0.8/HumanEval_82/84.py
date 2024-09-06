
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    #Your code here
    if len(string) <= 1:
        return True
    for i in range(2, len(string)):
        if (string[i] == '0') or (string[i] == '1'):
            continue
        if string[0] == '0' or string[0] == '1':
            continue
        if string[i] == string[0]+string[1]:
            continue
        if len(string) % i == 0:
            return False
    return True
