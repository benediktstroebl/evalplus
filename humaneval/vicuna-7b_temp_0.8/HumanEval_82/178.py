
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if string is empty
    if len(string) == 0:
        return False

    # Check if string is a digit
    if not string.isalpha():
        return False

    # Check if the length of the string is odd
    if len(string) % 2 == 0:
        return False

    # Initialize a variable to store the count of divisors
    divisors = 0

    # Check if the length of the string is prime
    for i in range(2, len(string)):
        divisors += 1
        if divisors % string[i] == 0:
            return False

    return True
