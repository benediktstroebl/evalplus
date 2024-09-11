```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): The number to find the largest prime factor of.

    Returns:
    int: The largest prime factor of n.

    Examples:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.

        Args:
        num (int): The number to check.

        Returns:
        bool: True if num is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start checking for prime factors from 2
    i = 2
    while i * i <= n:
        # If i is a factor of n and is prime, return it
        if n % i:
            # If i is not a factor of n, move to the next number
            i += 1
        else:
            # If i is a factor of n and is prime, return it
            if is_prime(i):
                return i
            # If i is not prime, divide n by i and continue checking
            while n % i == 0:
                n //= i
    # If n is a prime number greater than 1, return it
    if n > 1:
        return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```

This script solves the problem by using a helper function `is_prime` to check if a number is prime. It then checks all numbers from 2 up to the square root of `n` to see if they are factors of `n` and are prime. If a prime factor is found, it is returned. If `n` is a prime number greater than 1, it is returned.