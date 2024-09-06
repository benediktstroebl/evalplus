
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Define helper function to check if number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Define helper function to check if the string is a prime number
    def is_prime_string(string):
        # Check if the string is empty
        if len(string) == 0:
            return False

        # Check if the string is a single digit number
        if len(string) == 1:
            return is_prime(int(string))

        # Iterate through the string
        for i in range(2, len(string)):
            # Check if the number is divisible by the previous digit
            if string[i - 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and is_prime(int(string[i - 1]) * 10 + int(string[i])):
                return False

        return True

    # Check if the string is a prime number
    return is_prime_string(string)
