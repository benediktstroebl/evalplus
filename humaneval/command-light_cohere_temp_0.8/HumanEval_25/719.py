```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This function uses the sieve of Eratosthenes to find prime factors in a given number. 

It works by iteratively marking the multiples of numbers from 2 up in a list, and then checking if the remaining numbers are prime. The function returns a list of the prime factors found.