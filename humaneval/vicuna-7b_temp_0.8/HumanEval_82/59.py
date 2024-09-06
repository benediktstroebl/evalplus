
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string is empty or if it only contains whitespace
    if not string or string.strip() == '':
        return True

    # Initialize the variable 'i' to 2
    i = 2

    # Loop over each character in the string
    while True:
        # Check if the remainder of dividing i by the previous character is zero
        if string[i-1] not in ['0','1','2','3','4','5','6','7','8','9']:
            # If it is not, then the string is not prime and we can return False
            return False

        # If the remainder is zero, then the string is prime
        i += 1

    # If we reach this point, then the string must be prime
    return True