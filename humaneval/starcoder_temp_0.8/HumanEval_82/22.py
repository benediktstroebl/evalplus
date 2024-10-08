
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # your code here
    if len(string) == 1:
        return False
    elif len(string) == 2:
        return True
    else:
        if len(string) % 2 == 0:
            return False
        else:
            for i in range(3, len(string), 2):
                if string[:i] == string[:i][::-1]:
                    return False
    return True
