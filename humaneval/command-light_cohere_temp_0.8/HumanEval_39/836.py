```python
def prime_fib(n: int):
    if n <= 1:
        return n
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            return i
    return n
```