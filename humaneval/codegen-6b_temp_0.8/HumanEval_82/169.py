
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    import math

    if len(string) < 2:
        return True
    elif len(string) == 2:
        return True if string[0] == string[1] else False
    else:
        for n in range(2, math.ceil(math.sqrt(len(string)))):
            print(n)
            if len(string) % n == 0:
                print(' ')
                return False
    return True

