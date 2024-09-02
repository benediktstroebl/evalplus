
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a for loop to iterate through the string
    for i in range(1, len(string)):
        # Check if the string length is divisible by any number except for 1
        if not (string[i] == '1' or string[i] % i == 0 for i in range(2, len(string)+1)):
            return True
    return False