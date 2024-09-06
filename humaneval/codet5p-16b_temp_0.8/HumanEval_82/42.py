
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
        return True
    elif len(string) % 2 == 0:
        return False
    else:
        count = 0
        for i in range(len(string)):
            if i % 2!= 0:
                count += 1
        if count == len(string) / 2:
            return True
        else:
            return False

