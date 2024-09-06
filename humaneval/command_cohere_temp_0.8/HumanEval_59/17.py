```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
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
This approach optimizes the process of finding the largest prime factor. It first checks for the evident factors of 2. Following that, it iterates through numbers in ascending order, starting from 3, to identify composite factors, dividing n by each one. This method eliminates the need for multiple divisions for each potential prime factor, making it more efficient for larger numbers.