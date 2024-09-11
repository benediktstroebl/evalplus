```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    :param n: The number to find the largest prime factor of
    :return: The largest prime factor of n
    """

    # Initialize the largest factor to 1
    largest_factor = 1

    # Start checking from the smallest prime number
    i = 2

    # Continue checking until we reach the square root of n
    while i * i <= n:
        # If n is divisible by i, then i is a factor of n
        if n % i:
            # If n is not divisible by i, increment i by 1
            i += 1
        else:
            # If n is divisible by i, update the largest factor and divide n by i
            largest_factor = i
            n //= i

    # If n is still greater than 1, then it is a prime number and is the largest factor
    if n > 1:
        largest_factor = n

    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple trial division method to find the largest prime factor of a given number. It starts from the smallest prime number (2) and continues checking every number until it finds a factor that divides the number. The process is continued until the square root of the number is reached, as any factor larger than the square root would have a corresponding factor smaller than the square root.