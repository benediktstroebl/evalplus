

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO: Write a function to find the largest prime factor of a number.
    # Your function should assume that the input number is positive and not a prime.
    # The function should return the largest prime factor of the input number.
    
    # A prime number is a positive integer that is divisible only by 1 and itself.
    # The largest prime factor of a number is the largest prime number that divides the number.
    # To find the largest prime factor of a number, we can check all the prime numbers up to the square root of the number,
    # and take the largest one that divides the number.
    # For example, the largest prime factor of 13195 is 29, because the largest prime number that divides 13195 is 29,
    # which is the largest prime number that is less than or equal to the square root of 13195 (about 20.92).
    # However, if the number is very large, we may need to use more efficient algorithms to find the largest prime factor.
    
    # TODO: Implement the function using a brute-force approach by checking all the prime numbers up to the square root of the number.
    # You can use a loop to check all the prime numbers up to the square root of the number, and store the largest prime factor that divides the number in a list.
    # If there are multiple largest prime factors, only return the largest one.
    
    # For example, the following code uses a brute-force approach to find the largest prime factor of 2048:
    # largest_prime_factor(2048)
    # The function returns a list of prime numbers that divide 2048, and the largest prime factor of 2048 is 2:
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # The largest prime factor of 2048 is 2, which is the largest prime number that divides 2048 and is less than or equal to the square root of 2048 (about 15.84).
    
    # If the number is
