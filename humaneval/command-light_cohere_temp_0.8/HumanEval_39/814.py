```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    a, b = 3, 5  # a and b are prime factors
    for i in range(5, n + 2, 2):
        if a * i == b:
            break
    return b
``` 
This code defines a Python function `prime_fib` which calculates the n-th Fibonacci number that is also prime. It returns the maximum possible prime factor `b` for a given number `n`.