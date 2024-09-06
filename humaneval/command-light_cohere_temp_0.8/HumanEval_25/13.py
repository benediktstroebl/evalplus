```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        for i in range(3, int(n**.5) + 1, by=2):
            if n % i == 0:
                factors.append(i)
                n = n // i
    factors.append(n)
    return factors
```
This function uses the Sieve of Eratosthenes algorithm to find all prime factors of a given number, returning them in order from smallest to largest. The algorithm checks divisibility with numbers ranging from 2 to the square root of the input number.