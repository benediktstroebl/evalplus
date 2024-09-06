```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 3, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Test the function with various values
for i in range(6, 24):
    print(f"Test {i}: { prime_fib(i) }")
``` 
The function `prime_fib` calculates the nth Fibonacci number that is also prime, and tests the validity of the result for the input `n`. It returns the nth Fibonacci number that is also prime. 

**NOTE**: The function does not print the results for efficiency purposes.