
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if not string:
        return False
    else:
        count = 0
        for letter in string:
            count += 1
        if count == 2:
            return True
        elif count == 1:
            return False
        else:
            return prime_length(string[1:])


