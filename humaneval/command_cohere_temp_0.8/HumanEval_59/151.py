```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Write n as 2^a * 3^b * 5^c * ... * p_k^l
    # Where a >= 0, b >= 0, c >= 0, ...
    # l >= 0, and p_k is the largest prime factor
    exp = 0
    for prime in PRIMES:
        exp += n // prime
    n = n // 2 ** exp
    # Return n if n is a prime
    if n == 2:
        return n
    # Return 2 if n is 1
    if n == 1:
        return 2
    # Write n as n = 2 * p1
    # Return p1, the largest prime factor
    return n - 1
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
```