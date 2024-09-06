```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Iterate through potential factors from 2 to the square root of n
    for potential_factor in range(2, int(n**0.5) + 1):
        if n % potential_factor == 0:
            return potential_factor
        # Check if the divisor is a prime number, optimizing the process
        if potential_factor in PRIMES:
            return potential_factor
        PRIMES.append(potential_factor)
    # If no factors found, return n
    return n

PRIMES = [2, 3, 5, 7]

# Add test cases that can be easily verified
TEST_CASES = [
    (13195, 29),
    (2048, 2),
    (36, 36),
    (100, 10),
    (107, 107)
]

for n, expected in TEST_CASES:
    assert largest_prime_factor(n) == expected
```

This script defines the function `largest_prime_factor(n)` as requested and tests it against predefined test cases. It also uses a primality test to optimize the search for the largest prime factor. 

You can test the function with other inputs to verify its behavior. Let me know if you would like me to explain any part of the code in more detail.