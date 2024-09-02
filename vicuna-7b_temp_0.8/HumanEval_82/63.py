
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
    if len(string) == 0:
        return False

    # Check if the string is a single digit
    if len(string) == 1:
        return True

    # Check if the string is a prime number
    for i in range(2, int(len(string)**0.5)+1):
        if string[0] == '1' and string[1:] % i == 0:
            return False
        if string[0] != '1' and string[1:] % i == 0:
            return False

    return True
