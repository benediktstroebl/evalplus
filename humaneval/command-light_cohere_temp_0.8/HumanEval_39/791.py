```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    prime_fib = 6
    for i in range(7, n + 1):
        if n % i == 0:
            prime_fib = i
        elif n > prime_fib:
            prime_fib = n
    return prime_fib
```