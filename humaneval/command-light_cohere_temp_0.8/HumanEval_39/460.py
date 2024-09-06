Here's the solution:
```python
def prime_fib(n):
    if n <= 1:
        return n
    for i in range(2, n + 1):
        if is_prime(i) and not_prime(i * i):
            return i
    return n

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True

def not_prime_ sqrt(n):
    return math.sqrt(n)

def prime_fibonacci(n):
    return prime_fib(n)
```

This Python code defines a function `prime_fib` that calculates and returns the n-th Fibonacci number that is also prime. The function uses an nested loop to test numbers from 2 up to n for primality. The `is_prime` function is used to determine if a number is prime, and the `not_prime` function checks for divisibility by squares of other numbers. The `prime_fibonacci` function then calls `prime_fib` with the desired value of n and returns the result.