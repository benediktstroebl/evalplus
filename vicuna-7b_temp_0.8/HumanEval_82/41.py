
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n, factor_list):
        """Check if a number is prime by checking if it is divisible by any
        number in the list of factors
        """
        for p in factor_list:
            if n % p == 0:
                return False
        return True

    # Create a list of factors that could potentially divide the length of the string
    factors = [2]
    length = len(string)
    while length > 1:
        factors.append(length)
        length //= factors[-1]

    # Check if the length is divisible by any factor in the list
    if any(is_prime(length, factors) == False for factors in factors):
        return False
    else:
        return True
