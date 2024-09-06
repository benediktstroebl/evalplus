```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    if n % 5 == 0:
        return 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6
    return 2
``` 
This code provides a function that calculates and returns the n-th Fibonacci number that is also prime, by performing a series of checks to exclude non-prime numbers.