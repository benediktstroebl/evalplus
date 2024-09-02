
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    prime = True
    length = len(string)
    if length <= 1:
        return True
    elif length % 2 == 0:
        prime = False
    else:
        for n in range(3, int(length / 2) + 1, 2):
            if length % n == 0:
                prime = False
    return prime


