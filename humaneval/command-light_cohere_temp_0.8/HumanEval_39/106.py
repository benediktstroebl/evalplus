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
    return n
``` 
This code defines a function `prime_fib` that calculates the nth Fibonacci number and determines whether it's also prime. The function employs a `if-else-else` statements and checks for divisibility by 2 and 3 before attempting larger prime numbers.