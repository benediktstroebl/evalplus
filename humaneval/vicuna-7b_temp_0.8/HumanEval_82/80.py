
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here
    # You can use the Sieve of Eratosthenes algorithm to quickly
    # determine if a number is prime or not
    for i in range(2, int(string)**0.5 + 1):
        if string[i:i+2] == string[i+2:i+2+string[i:i+2]):
            return False
    return True
