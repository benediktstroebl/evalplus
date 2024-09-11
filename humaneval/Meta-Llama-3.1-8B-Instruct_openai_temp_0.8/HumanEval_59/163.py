```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    :param n: The number to find the largest prime factor of.
    :return: The largest prime factor of n.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Initialize the largest factor as 1
    largest_factor = 1

    # Start from 2, the smallest prime number
    i = 2

    # Continue until i is less than or equal to the square root of n
    while i * i <= n:
        # If n is divisible by i, then i is a prime factor
        if n % i:
            # If n is not divisible by i, increment i by 1
            i += 1
        else:
            # If n is divisible by i, update the largest factor and divide n by i
            largest_factor = i
            n //= i

    # If n is a prime number greater than 1, then it is the largest prime factor
    return max(largest_factor, n)

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script works by iterating from 2 to the square root of `n`, checking if `n` is divisible by the current number. If it is, then the current number is a prime factor, and we update the largest factor and divide `n` by the current number. If it's not, we increment the current number by 1. Finally, if `n` is greater than 1 after the loop, then it is a prime number and the largest prime factor.