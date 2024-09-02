
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
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function to check if a string is a prime number
    def is_prime_string(n):
        n = int(n)
        if n <= 1:
            return False
        # Check if the string contains only digits
        if '0123456789' not in str(n):
            return False
        # Check if the string length is equal to 1 or 2
        if len(n) == 1 or len(n) == 2:
            return True
        # Check if the string length is greater than 2
        for i in range(3, len(n)):
            # Check if the string contains only odd digits
            if int(''.join([str(d) for d in n])) % 2 != 0:
                return False
        return True

    # Call the is_prime function and check if the returned value is True
    if is_prime(int(string)) and is_prime_string(int(string)):
        return True
    else:
        return False
