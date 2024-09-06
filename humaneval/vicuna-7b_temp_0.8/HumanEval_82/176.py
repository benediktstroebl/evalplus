
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # A list that stores the prime numbers up to the square root of the length
    # of the input string.
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # For each character in the input string
    for i in range(1, len(string)):
        # If the current character is a prime number
        if string[i] in prime_numbers:
            # If the remaining characters of the input string are all zeroes
            if all(c == 0 for c in string[i:]) and len(string[i:]) > 1:
                return True
        # If the current character is not a prime number
        else:
            # If the remaining characters are all zeroes
            if all(c == 0 for c in string[i:]):
                return True
    return False
