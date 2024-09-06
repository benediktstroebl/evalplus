
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    else:
        x = 2
        for y in range(1, len(string)):
            if x != len(string) and x*(len(string)-1) == y:
                x += 1
                continue
            else:
                return False
    return True
