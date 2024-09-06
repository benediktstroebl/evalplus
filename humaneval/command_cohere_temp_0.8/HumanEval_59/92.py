```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Write n as 2^a * 3^b * 5^c * ... * p_k^l
    # Where a, b, c ... , l are maxues 0, 1, ... , k-1
    # respectively
    # So we take the max of a, b, c, ... , l to return
    max_power = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            pow = 0
            while n % i == 0:
                n //= i
                pow += 1
            if pow > max_power:
                max_power = pow
    if n > 1:
        max_power += 1
    return 2 ** max_power
```