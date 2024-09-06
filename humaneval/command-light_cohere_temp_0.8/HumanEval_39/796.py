```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            return i
        i += 6
    return next((i + 1) for i in range(2, n + 1) if n % i == 0)
```
This function takes an integer n as input and returns the n-th Fibonacci number that is prime. It uses an back-on approach, where it tests for divisibility by 2 and 3, and then uses a while loop to find the next prime factors.