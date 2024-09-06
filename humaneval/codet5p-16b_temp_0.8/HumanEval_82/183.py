
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
    if len(string) > 1:
        if len(string) % 2 == 0:
            return False
        else:
            return not math.prod([x for x in range(2,int(len(string)/2+1)) if string.count(string[x]) > 0])
    else:
        return True

