
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Create a list of all prime numbers less than 100
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Check if the length of the string is less than 2
    if len(string) < 2:
        return True

    # Check if the length of the string is equal to 2
    if len(string) == 2:
        return False

    # Check if the length of the string is 3
    if len(string) == 3:
        return True

    # Loop through all characters in the string
    for char in string:
        # Check if the current character is 2, 3, 5, 7, or 9
        if char in ['2', '3', '5', '7', '9']:
            return True

        # Check if the current character is 4, 6, 8, or 10
        elif char in ['4', '6', '8', '10']:
            # Loop through all characters in the string
            for next_char in string:
                # If the next character is 2, 3, or 5, return True
                if next_char in ['2', '3', '5']:
                    return True

            # If the next character is 4, 6, 8, or 10, return False
            return False

    # If the string has no vowels, return True
    if 'aeiou' not in string:
        return True

    # If the string has at least one vowel, return False
    return False