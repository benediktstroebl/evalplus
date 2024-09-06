```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        for i in range(2, n):
            is_prime = True
            for j in range(2, int(i**0.25)):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                return i
        return n
```