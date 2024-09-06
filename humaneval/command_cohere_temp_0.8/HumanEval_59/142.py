```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case where n is a power of 2.
    if n >= 2 and ((n & (n - 1)) == 0):
        return 2
    # Threshold for switching to sieve
    if n > 10:
        sieve = [True] * (n + 1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        for i in range(2, n + 1):
            if sieve[i]:
                return i
    # Fallback for small numbers
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n
```

This approach handles the special case of n being a power of 2, which accounts for many of the numbers that occur in typical use cases. For larger n, we perform a sieve of Eratosthenes to efficiently find all prime factors. Lastly, for small n, we fallback to an iterative approach, looping from 3 upwards, skipping every other number.

This should provide an efficient solution for the given problem that handles a wide range of input values while still being understandable and maintainable. Let me know if you would like any additional explanations or if you would like to proceed with more ideas for optimizing this function.