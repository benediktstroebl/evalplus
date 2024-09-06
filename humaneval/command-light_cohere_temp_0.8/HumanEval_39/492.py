Here is a Python script with a self-contained function that solves the problem of finding the n-th Fibonacci number that is prime:
```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        prime_sum = 2 + 3
        for i in range(5, n + 1, 2):
            prime_sum += prime_sum // i
        return prime_sum

print(prime_fib(5))
```

The code defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime. It starts by checking whether the `n` is a positive integer, and if not, raises an error. Then, for n >= 5, it uses a loop to calculate the sum of the prime numbers up to the given Fibonacci number.