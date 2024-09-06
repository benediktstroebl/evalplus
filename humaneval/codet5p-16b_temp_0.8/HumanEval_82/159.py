
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if len(string) > 1 and len(string) % 2 == 0:
        return False
    else:
        num = 3
        while num <= int(len(string)):
            if len(string) % num == 0:
                return False
            num += 2
        return True

