
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # return prime_length(string)

    # If the string is empty or 1 character long,
    # it is not a prime length.
    if len(string) < 2:
        return False

    # Create a set of characters from the input string.
    char_set = set(string)

    # Count the number of unique characters in the set.
    unique_chars = len(char_set)

    # Check if the number of unique characters is prime.
    return is_prime(unique_chars)

