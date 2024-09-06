
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a list to store prime numbers that are less than the square root of the
    # string length
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    # Check if the string length is divisible by any prime number in the list
    for number in prime_numbers:
        if len(string) % number == 0:
            return False
    
    # If none of the prime numbers in the list could divide the string length,
    # then the string length must be prime
    return True
