
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string is empty
    if not string:
        return False

    # Check if the string is '1'
    if string == '1':
        return True

    # Loop through the string and check if the length of the substring
    # starting at the current position is a prime number or if it is empty
    for i in range(1, len(string)):
        if len(string[i:]) > 1 and is_prime(string[i:]):
            return True

    return False