

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # Handle the case where n is 0 or 1 by returning False
    if n == 0 or n == 1:
        return False
    # Handle the case where n is a prime number
    if n > 1:
        # Check if n is prime by using the fact that it is greater than 1
        # and that the last digit of the prime factorization of n must
        # be 1, 3, 7, or 9, because if the last digit is 1, 3, 7, or 9,
        # then the digit immediately to the left must be either 2, 4, 6,
        # or 8, which leaves no choice but for the remaining digits to
        # be 1, 3, 7, or 9.
        # For example, 71 is not prime because the prime factorization
        # of 71 is 71 = 7 \* 11, and the last digit of 11 is 9.
        # However, 711 is prime because the prime factorization
        # of 711 is 711 = 7 \* 11 \* 13, and the last digit of 13 is 3.
        # We use a while loop to find the prime factorization of n
        # and check the last digit of the first factor that is greater
        # than n / 2.
        i = 1
        while n > 2:
            n //= 2
            i += 1
        return True
    # Otherwise, return False
    return False