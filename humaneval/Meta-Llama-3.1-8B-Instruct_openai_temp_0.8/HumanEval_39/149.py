```python
import math

def is_prime(num: int) -> bool:
    """
    checks if a number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """
    generates the nth Fibonacci number
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if i == n:
                return fib_num
            i += 1
        else:
            i += 1

# example usage
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates the nth Fibonacci number, and `prime_fib` uses these helper functions to find the nth Fibonacci number that is also prime. The example usage demonstrates how to call `prime_fib` with different inputs.