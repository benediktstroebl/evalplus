
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # check to see if the string has even number of characters
    if len(string) % 2 == 0:
        return False

    # check to see if the number of characters is a prime number
    divisors = []
    for n in range(1, len(string) + 1):
        if len(string) % n == 0:
            divisors.append(n)

    if len(divisors) <= 2:
        return True

    return False
