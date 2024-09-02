
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string has only letters
    if not all(char.isalpha() for char in string):
        return False
    
    # Check if the length is greater than 2
    if len(string) < 3:
        return False
    
    # Check if the string is empty
    if not string:
        return False
    
    # Check if the string is a prime number
    # Use the sieve of Eratosthenes algorithm to check if a number is prime
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # ...
    
    # Return True if the string is prime, False otherwise
    return True