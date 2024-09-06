
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # in a prime length the number of letters must be a prime number
    # To find if a number is prime,
    # we can simply check if it has any factors other than 1 and itself.
    # If it does, then it is not a prime number

    if len(string) == 1:
        return True
    elif len(string) == 2:
        return True
    else:
        for i in range(2, len(string)):
            if string % i == 0:
                return False
        return True
