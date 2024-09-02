
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string is empty or not
    if len(string) == 0:
        return False
    # Create a list of characters in the string
    characters = string.split()
    # Create a list of prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # Iterate over the prime numbers
    for num in prime_numbers:
        # Check if the string has a length divisible by this number
        if len(string) % num == 0:
            return False
    # If no prime number is found, the string is prime
    return True
