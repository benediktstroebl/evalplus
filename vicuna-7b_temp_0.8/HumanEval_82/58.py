
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a generator to iterate over the string
    # Use the "next" function to access the next item in the iteration
    for x in string:
        # If the string length is prime, return True
        if len(string) == 1:
            return True
        # If the length of the current character is not prime, return False
        if len(str(x)) != 1:
            return False