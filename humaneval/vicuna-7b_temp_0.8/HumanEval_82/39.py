
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Define a variable for the number of characters in the string
    n = len(string)
    # Define a variable to store the count of factors
    factors = 0
    # Iterate through the characters in the string
    for i in range(n):
        # Check if the current character is prime
        if n % i == 0:
            factors += 1
            if factors == n:
                return True
    return False
