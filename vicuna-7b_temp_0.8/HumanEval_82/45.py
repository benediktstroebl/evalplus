
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Write a function that takes a string as input
    # Check if the length of the string is prime or not
    # Return True if it's prime and False otherwise
    if len(string) > 2:
        for i in range(2, len(string)):
            if string[i:i+2] == string[i:i+2][::-1]:
                return False
        return True
    return False
