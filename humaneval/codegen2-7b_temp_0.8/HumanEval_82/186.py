
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
    elif len(string) == 2:
        return True
    else:
        return all(i >= 2 for i in range(2, int(len(string) / 2) + 1)) and prime_length(string[1:])

