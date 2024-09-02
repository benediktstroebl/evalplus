
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    length = len(string)

    if length == 2 or length == 3 or length == 5 or length == 7 or length == 11 or length == 13 or length == 17:
        return True
    elif length == 4 or length == 6 or length == 8 or length == 9 or length == 12 or length == 14 or length == 16:
        return False
    else:
        prime = True
        for i in range(2, length - 1):
            if length % i == 0:
                prime = False
        return prime

