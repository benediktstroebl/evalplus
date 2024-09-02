
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a dictionary to store the prime numbers less than the square root of n
    prime = [True] * (1000000)
    for i in range(int(sqrt(len(string)) + 1)):
        if string[i:i+2] in prime:
            return True
    return False
