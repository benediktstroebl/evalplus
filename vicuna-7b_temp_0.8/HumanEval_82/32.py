
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Define a dictionary to store prime numbers and their lengths
    prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
    
    # Use a for loop to iterate through the characters in the string
    for character in string:
        # If the character is not a digit, it is not prime
        if character not in '0123456789':
            return False
    
        # Add 1 to the current prime number and check if the new number is still prime
        for i in range(1, len(prime_numbers)):
            if (prime_numbers[i] + 1) % character == 0:
                return False
    
        # If we have reached the end of the string and we have not found a composite number, it is prime
        return True