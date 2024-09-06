
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 2 or len(string) == 3:
        return True
    elif len(string) < 3:
        return False
    elif len(string)%2 == 0 or len(string)%3 == 0:
        return False
    else:
        divisor = 5
        for divisor in range(5, int(len(string)**0.5)+1, 6):
            if len(string) % divisor == 0:
                return False
        return True









