Here is a Python script that defines a self-contained function to calculate the n-th Fibonacci number that is also prime, along with testing:
```python
import math

def prime_fib(n):
    """
    This function calculates the n-th Fibonacci number that is also prime.
    It returns the F(n) if it is a prime and otherwise returns infinity.
    """
    prime_test = [True, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    for num in prime_test:
        if num == prime_fib(num):
            return num
    return infinity

print(prime_fib(100))  # Should print the 100th prime Fibonacci number
```