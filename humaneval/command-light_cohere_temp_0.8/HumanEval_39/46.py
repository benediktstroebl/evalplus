```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        a = prime_fib(n // 2)
        if a == 2 or a == 3:
            return a
        else:
            return _prime_fib(n)

def _prime_fib(n: int):
    if n <= 1:
        return n
    i = 5
    while i * i <= n:
        if n % i == 0:
            return i
        i += 6
    return 2

# Example usage
print(prime_fib(5))
```