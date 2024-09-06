
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    number = int(string)
    i = 2
    if number == 1:
        return False
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True
