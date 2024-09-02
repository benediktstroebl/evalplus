
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    def is_prime(n, factors):
        """Function to check if a number is prime
        Args:
            n: The number to check
            factors: A list of integers that are already checked
        Returns:
            True if n is prime, False otherwise
        """
        # Your code here

    def prime_length(string):
        """Function to check if a string is a prime number
        Args:
            string: The string to check
        Returns:
            True if the string length is a prime number, False otherwise
        """
        # Your code here
        # Use is_prime function
        length = len(string)
        for i in range(2, length):
            if string[i:i+2] in factors:
                return False
        return True
        # Your code here