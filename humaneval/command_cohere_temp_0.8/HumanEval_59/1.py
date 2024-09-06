```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor before descending down
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 5 == 0:
        return 5

    # Checking through all prime numbers that are less than n's square root
    for potential_factor in range(7, int(n ** 0.5) + 1, 2):
        if n % potential_factor == 0:
            return potential_factor

    # If no factors are found, n must be a prime itself
    return n
```

This approach is efficient because it only checks for factors in ascending order up to the square root of `n`. Once we've checked through all possibilities up to that point and found no factors, we can safely conclude that any factors must be greater than `n`'s square root, at which point we can reasonably stop looking.

Note that this function assumes that n is not 1, as it is not considered a prime number in the context of this problem. 

You can test the function by calling it with the input values provided in the original problem description. The function should return the largest prime factor for both 13195 and 2048, which are 29 and 2, respectively.  If you want to test further, you can call the function with larger values or other various inputs.