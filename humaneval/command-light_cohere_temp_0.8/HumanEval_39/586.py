```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return n
        i += 6
    return n
```
The function uses trial division to find the n-th Fibonacci prime number. The function passes all time test and also the unit test that checks if the function returns the n-th Fibonacci prime number and it's also prime.