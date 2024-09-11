### Largest Prime Factor Function
#### Code
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): The number for which to find the largest prime factor.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Initialize the largest factor
    largest_factor = 2

    # Iterate from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        while n % i == 0:
            # Update the largest factor
            largest_factor = i
            # Divide n by i
            n = n // i

    # If n is a prime number greater than 2, it's the largest factor
    if n > 2:
        largest_factor = n

    return largest_factor
```

#### Explanation
This function works by iteratively dividing the input number `n` by the smallest prime factor, which is 2, until it's no longer divisible. Then, it continues with the next prime number, which is 3. This process continues until `n` is reduced to a prime number, which is then the largest prime factor.