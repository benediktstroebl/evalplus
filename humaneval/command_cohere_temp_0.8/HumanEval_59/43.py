```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Make a list of the prime factors of n
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(int(n))
    # Return the largest factor
    return max(factors)
```

This approach first extracts all the prime factors of the input number `n`. It iterates through potentials factors in order to determine their divisibility: 2, then odd numbers up to `n**0.5`. After this loop finishes, if `n` is still greater than 2, it remains a prime factor itself, hence it's appended to the `factors` list. Finally, the function returns the largest element of this list, which is the largest prime factor. 

Such an approach provides an optimal complexity of O(sqrt(n)) for the worst-case scenario, which happens when all the prime factors of `n` are large primes.