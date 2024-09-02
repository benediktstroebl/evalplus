
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check for empty string
    if len(string) == 0:
        return False

    # check for numbers
    for char in string:
        if char.isdigit():
            return False

    # check for special characters
    for special in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '-', '_', '+', '~']:
        if special in string:
            return False

    # check for prime numbers
    for i in range(2, int(len(string)**0.5) + 1):
        if is_prime(string[i:], string[i:]) or string[i:i+2] in ['0', '1']:
            return False

    return True
