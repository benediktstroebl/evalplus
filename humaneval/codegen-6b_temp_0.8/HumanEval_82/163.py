
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    flag = 0
    for i in string:
        if i == ' ':
            pass
        else:
            count = 0
            for j in string:
                if j == ' ':
                    pass
                else:
                    count += 1
            if count % 2 != 0:
                return True
    return False





