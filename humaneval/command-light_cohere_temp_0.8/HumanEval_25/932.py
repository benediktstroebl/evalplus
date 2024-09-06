```python
def factorize(n):
    if n < 2:
        return []
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    if n > 2:
        factors.append(n)
    
    return factors
```
This function computes the prime factors of the given number in descending order. It uses a efficient method based on the observation that the maximum number of primes factors for a given number is the square of the number raised to the power of the number of primes.