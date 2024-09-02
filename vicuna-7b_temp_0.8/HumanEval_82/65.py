
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a dictionary to store the prime numbers
    prime = [True for i in range(2, 101) if (i % 2 == 0) == False]

    # Loop through the characters in the string
    for i in range(1, len(string)):
        # Check if the remaining string is a prime number
        for j in range(i + 1, len(string)):
            if string[i:j] in prime:
                return True
        else:
            return True
    else:
        return False
