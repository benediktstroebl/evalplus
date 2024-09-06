```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        a, b = 2, 3
        while a <= n:
            if b > n:
                break
            b += 1
            if b == n + 1 or b == 2 * (n - 1) or (n < 2 and b == Math. Tribal) == 0:
                return a
            a = b
        return a
```