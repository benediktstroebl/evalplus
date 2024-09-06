
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Function to check if a number is prime or not
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Check if the string is empty or not
    if not string:
        return True

    # Initialize the variable i with 2
    i = 2

    # Loop through the characters in the string
    for char in string:
        # Loop through the characters in the string
        for j in range(i**2, len(string)):
            # Check if the string is divisible by i
            if string[j:j+i] == str(i):
                return False
        # Increment the i variable by 1
        i += 1

    # If the loop completes without finding a divisor,
    # then the string must be prime
    return True
