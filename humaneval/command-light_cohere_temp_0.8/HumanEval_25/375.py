```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
The function uses the sieve of Eratosthenes algorithm to find prime factors of a given number and returns a list of integers in which each integer occurs that many times in the factorization of the input number.