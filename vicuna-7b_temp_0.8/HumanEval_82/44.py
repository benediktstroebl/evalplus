
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use the sieve of Eratosthenes algorithm to check if a number is prime
    # Make a list of all prime numbers less than the square root of n
    # Then check if the input string length is in the list
    # If it is, return True
    # If it is not, return False
    # If the length is greater than the square root of n, return False
    # If the length is less than 2, return False
    
    # Initialize a list of prime numbers less than the square root of n
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Check if the input string length is in the list of prime numbers
    for i in range(1, len(primes)):
        if primes[i-1] <= int(string) <= primes[i]:
            return True
    return False
