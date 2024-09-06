```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Write n as 2^a * 3^b * 5^c * ... * p_k^z
    # Where p_k is the largest prime factor
    z = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            z += 1
            while n % i == 0:
                n //= i
        if n == 1:
            break
    # Restore n in case it was completely factored out
    if n < 1:
        n = 1
    return 2 ** a * 3 ** b * 5 ** c * p_k ** z
```

Where a, b, c, ... = largest prime factors of n.
This solution has an average time complexity of O(log(n)).