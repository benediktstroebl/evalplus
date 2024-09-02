
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Write code to determine if the string is a prime number
    # If it is, return True
    # If it is not, return False
    # If the string is empty, return False
    if string == "":
        return False
    # Check if the length is less than 2
    if len(string) < 2:
        return False
    # Check if the length is prime
    for i in range(2, len(string)):
        # If the length is divisible by any number
        # except 2, return False
        if (string[i:i+2] == string[i] + string[i+1] for _ in range(len(string))):
            return False
    return True
