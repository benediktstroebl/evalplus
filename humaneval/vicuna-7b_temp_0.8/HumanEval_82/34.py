
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    for i in range(2, string.length + 1):
        if string[i] == '1':
            continue
        if string[i] != '2':
            for j in range(i + 1, string.length):
                if (string[i-1] != '1' and string[i-1] % 2 == 0) and (string[j] % 2 == 0):
                    return False
                elif string[i-1] % 2 != 0 and string[j] % 2 == 0:
                    return False
    return True