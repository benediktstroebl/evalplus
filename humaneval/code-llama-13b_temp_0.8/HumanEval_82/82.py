
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    n = len(string)
    if n == 1 or n == 2:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    counter = 5
    while counter ** 2 <= n:
        if n % counter == 0 or n % (counter + 2) == 0:
            return False
        counter += 6

    return True
    
