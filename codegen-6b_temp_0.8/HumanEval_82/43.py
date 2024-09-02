
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # use the square_root function to determine if a string is a prime
    # this ensures a string of length 1 is a prime
    return all(square_root(ord(char)) < 1 for char in string)

