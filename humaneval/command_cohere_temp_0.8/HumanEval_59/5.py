```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    factor = n
    while factor % 2 == 0:
        factor //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while factor % i == 0:
            factor //= i
    if factor > 1:
        return factor
    else:
        return n
```

The function employs an optimized approach to find the largest prime factor. It repeatedly divides n by factors of 2, then factors of odd numbers 3 and greater. This strategy significantly reduces the number of divisions needed. The initial factorization by 2 optimizes the process, as most numbers have 2 as the largest factor. Consequently, for larger numbers, the time complexity is essentially O(log N), making the function highly efficient.