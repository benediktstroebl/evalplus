
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if string == "":
        return False
    for i in range(2, len(string)):
        if string[i] == " ":
            j = i + 1
            while string[j] == " ":
                j += 1
            if string[j] == " ":
                continue
        for k in range(i+1, len(string)):
            if string[i] == string[k] % 2 == 0:
                return False
    return True