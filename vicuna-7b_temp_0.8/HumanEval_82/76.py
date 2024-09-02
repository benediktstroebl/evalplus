
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a variable to check if the string is prime
    is_prime = True
    
    # Use a loop to iterate through the string
    for char in string:
        # If the string has repeating characters, it is not prime
        if char in string:
            is_prime = False
            break
        
        # If the string is long enough, check if it is prime
        if len(string) >= 2:
            if (string[0] != char or string[1] != char) and len(string) % (2 * len(string) // (len(string) // 2 - 1)) == 0:
                is_prime = False
    
    return is_prime
