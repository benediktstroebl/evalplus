```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    if n % 3 == 0:
        return 13
    pi = 23
    while pi * pi <= n:
        if n % pi == 0:
            return pi
        pi += 2
    return n

# Test the function
for i in range(6, 30):
    print(prime_fib(i), end=' ')
```