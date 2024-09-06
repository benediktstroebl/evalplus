
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    count = 0
    for i in string:
        count += 1

    if count == 2 or count == 3 or count == 5 or count == 7:
        return True
    elif count == 4 or count == 6:
        return False
    elif count % 2 == 0 or count % 3 == 0 or count % 5 == 0 or count % 7 == 0:
        return False
    else:
        return True

