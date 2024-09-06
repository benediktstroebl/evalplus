```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2: 
        factors.append(n)
    return max(factors)
```
The function iterates through potential factors from 2 to `n**0.5` (to account for both even and odd divisors), continuously dividing `n` by each potential factor until it's no longer divisible. This ensures that the function performance linearly proportional to `log(n)` (`O(n log(n))`). The maximum factor is returned, accounting for the possibility that `n` might be a prime larger than `n**0.5`. 

Here is an example usage of the function which verifies its correctness against the given problem statement:
```python
>>> largest_prime_factor(13195)
29
>>> largest_prime_factor(2048)
2
``` 
This function handles inputs appropriately, including handling the edge case where `n` is a prime number larger than `n**0.5`.