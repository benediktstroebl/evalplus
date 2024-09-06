
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_length = 0
    for i in range(len(string)):
        prime_length += 1
        if prime_length == 1 or prime_length == 2 or prime_length == 3 or prime_length == 5 or prime_length == 7 or prime_length == 11 or prime_length == 13 or prime_length == 17:
            return True
        else:
            return False
