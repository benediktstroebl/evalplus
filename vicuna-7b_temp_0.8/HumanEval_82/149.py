
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a list of prime numbers up to the square root of the input string
    primes = [x for x in range(2, int(len(string)**0.5) + 1) if is_prime(string[0] + string[1] + ... + string[len(string)-1])]

    # Check if the length of the string is a prime number
    for num in primes:
        if string.count(str(num)) == 1:
            return True
    return False
