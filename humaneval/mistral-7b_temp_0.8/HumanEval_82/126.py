
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # Check if string is empty
    if not string:
        return False

    # Convert string to list of characters
    string = list(string)

    # Initialize a list to store primes
    primes = []

    # Initialize a list to store non-primes
    non_primes = []

    # Initialize a variable to store the length of the string
    length = len(string)

    # Iterate over the list of characters
    for char in string:
        # Check if the character is a number
        if char.isdigit():
            # Check if the number is a prime
            if is_prime(int(char)):
                # If it is, add it to the list of primes
                primes.append(int(char))
            else:
                # If it is not, add it to the list of non-primes
                non_primes.append(int(char))

    # Check if the length of the string is a prime number
    if length in primes:
        return True
    else:
        return False

