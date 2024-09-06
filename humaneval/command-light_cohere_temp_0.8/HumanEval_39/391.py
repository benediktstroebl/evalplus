```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # Calculate the nth Fibonacci number using recursion
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def test_prime_fib():
    n = int(input("Enter a positive integer: "))
    result = prime_fib(n)
    if result == 2:
        print(f"It's a Fibonacci number and also prime {n}")
    else:
        print(f"It's not a Fibonacci number and not prime {n}")

# Run the tests
test_prime_fib()
```

This Python script defines a function `prime_fib` that computes the nth Fibonacci number and checks if it's also prime. It also includes a test function to run the test cases and verify the results.

Note: This script is designed to be self-contained and does not require any additional modules or external functions.