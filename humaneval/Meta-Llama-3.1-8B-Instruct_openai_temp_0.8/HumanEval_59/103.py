```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): An integer greater than 1.

    Returns:
        int: The largest prime factor of n.

    Example:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    # Initialize the largest factor to 2
    largest_factor = 2

    # Check if n is divisible by 2
    while n % 2 == 0:
        # Update the largest factor if necessary
        largest_factor = 2
        # Divide n by 2
        n = n // 2

    # Check for other prime factors
    for i in range(3, int(n**0.5) + 1, 2):
        # Check if n is divisible by i
        while n % i == 0:
            # Update the largest factor if necessary
            largest_factor = i
            # Divide n by i
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        # Update the largest factor if necessary
        largest_factor = n

    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

However, it's possible to optimize this function to run in less time for large inputs by implementing sieve of Eratosthenes. Here's the optimized version:

```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): An integer greater than 1.

    Returns:
        int: The largest prime factor of n.

    Example:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    # Create a boolean array, prime, of size n+1
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    # Iterate from 2 to sqrt(n)
    for p in range(2, int(n**0.5) + 1):
        # If p is a prime, mark as composite all the multiples of p
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    # Find the largest prime factor of n
    largest_factor = 2
    while n % 2 == 0:
        largest_factor = 2
        n = n // 2
    for p in range(3, int(n**0.5) + 1, 2):
        if prime[p]:
            while n % p == 0:
                largest_factor = p
                n = n // p
    if n > 2 and prime[n]:
        largest_factor = n

    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```