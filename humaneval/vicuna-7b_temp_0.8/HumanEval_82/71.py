
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n):
        # If n is even, it is not a prime
        if n % 2 == 0:
            return False
        # If n is odd, it is a prime
        return True

    # Create a list of numbers up to the square root of n
    nums = [n for n in range(2, int(n**0.5) + 1) if is_prime(n)]

    # If the length of the string is equal to the square root of a prime number
    # then the string is prime
    for i in range(len(string)):
        if string[i] == '*':
            # If there is an asterisk in the string, check if the remaining numbers
            # are prime
            for j in range(i+1, len(string)):
                if string[j] in nums:
                    return True
            return False
    return True
