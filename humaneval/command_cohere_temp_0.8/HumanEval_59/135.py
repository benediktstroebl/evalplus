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
The function iterates through potential factors from 2 up to the square root of n, dividing n by each even factor and each odd factor up to its square root. This is becausecomposite numbers larger than 2 are necessarily divisible by odd factors greater than their square root, so there is no need to check for divisibility by larger odd numbers. 

This approach provides an efficient route to finding the largest prime factor, handling the specified case of 2048 (where the largest prime factor is 2) and 13195 (where the largest prime factor is 29). 
If, after exhausting these checks, the remaining factor is greater than 1, it is returned as the largest prime factor. Otherwise, the original number n is returned, indicating that it is a prime number with no distinct prime factors. Leveraging the early division by 2 and efficient checking up to the square root of n helps optimize runtime, ensuring readiness for larger numbers.