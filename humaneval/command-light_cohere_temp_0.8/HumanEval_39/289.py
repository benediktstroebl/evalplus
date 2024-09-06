```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        a, b = 6, 7
        for _ in range(n - 4):
            a, b = b, a + b
        if a == b:
            return a
        elif a > b:
            a, b = b, a + b
        elif a == b + 2 and b > 2:
            return a
        return b
```