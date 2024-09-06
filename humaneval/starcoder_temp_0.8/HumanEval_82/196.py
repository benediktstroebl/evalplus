
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if not string:
        return False

    string = string.lower()

    # remove all non-alphanumeric characters
    string = re.sub('[^a-z0-9]', '', string)

    return len(string) in PRIMES

