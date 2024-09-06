```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Make a list of the prime factors of n
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n //= i
    if n > 2:
        pf.append(n)
    # Return the largest factor
    return max(pf)
```
The function iterates through potential prime factors from 2 to `n**0.5`. It only considers odd numbers to avoid even factors. For each potential factor, it checks if `n` is divisible. If it is, the factor is added to the list of prime factors, and `n` is divided by that factor until it is no longer divisible by that factor. This process efficiently finds all prime factors and ensures `n` is reduced to its largest prime factor. The maximum prime factor is then returned.  This approach provides an efficient O(sqrt(n)) algorithm for a slightly less naive approach that would be an O(n) algorithm.