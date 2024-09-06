```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        # Compute and return next prime factors
        prime = n
        while prime > 2:
            prime //= 2
            if prime % 2 == 0:
                break
        return prime
```