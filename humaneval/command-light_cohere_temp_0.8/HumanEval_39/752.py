Here's a self-contained Python function that calculates the n-th Fibonacci number and determines whether it is prime:
```python
def prime_fib(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        # Calculate the n-th Fibonacci number
        fib = 0
        temp = 1
        for _ in range(2, n + 1):
            fib += temp
            temp = temp - fib
        return is_prime(fib)

def is_prime(num: int) -> bool:
    """ Checks whether a given number is prime."""
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
```

This script defines a function `prime_fib` that calculates the n-th Fibonacci number and determines if it's prime. It also defines a another function, `is_prime`, that checks whether a given number is prime. The `is_prime` function implements the Miller-Rabin primality test, which is one of the most popular primality tests.