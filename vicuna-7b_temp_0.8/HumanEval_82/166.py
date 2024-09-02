
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Define a list of numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # Create a variable to store the result
    result = False
    # Iterate through all the characters in the string
    for char in string:
        # If the character is a digit, check if it is a prime number
        if char.isdigit():
            # Check if the number is in the list of prime numbers
            if char == int(char) % 1:
                result = True
        elif char == '1':
            result = True
    return result