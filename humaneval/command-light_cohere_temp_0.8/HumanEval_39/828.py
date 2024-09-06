```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 6
    else:
        a, b = 2, 3
        for _ in range(5):
            if a % b == 0:
                break
            a, b = b, a+b
        return a
```