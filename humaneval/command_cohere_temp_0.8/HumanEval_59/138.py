```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2: 
        factors.append(int(n))
    return max(factors)
```

This approach first checks if `n` is divisible by 2. If it is, it factors out the common factor and repeats the process until the number is reduced to 1. Then, it iterates through odd numbers from 3 to the square root of `n` (skipping every other number, i.e., every 2th number), factoring out each one until the number is reduced to 1. For any remaining prime factors, the algorithm finally appends them to the list of factors that cannot be further reduced. Finally, it returns the largest factor in this list.