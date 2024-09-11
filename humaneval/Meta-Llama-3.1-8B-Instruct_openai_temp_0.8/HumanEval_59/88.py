```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Parameters:
    n (int): The number to find the largest prime factor of.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Start from the smallest prime number, 2
    i = 2

    # While the divisor is less than or equal to the square root of n
    while i * i <= n:
        # If n is divisible by i, then i is a prime factor
        if n % i:
            # If n is not divisible by i, increment i by 1
            i += 1
        else:
            # If n is divisible by i, divide n by i and update the largest prime factor
            n //= i

    # At this point, n is the largest prime factor of the original number
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple trial division method to find the largest prime factor of a given number. It starts by dividing the number by the smallest prime number, 2, and continues dividing by increasing integers until it finds a divisor. If a divisor is found, it is the largest prime factor so far, and the number is divided by this divisor. This process is repeated until no more divisors are found, at which point the remaining number is the largest prime factor.