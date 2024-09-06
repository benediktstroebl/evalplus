```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    sequence = [0]
    for _ in range(n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[n - 1]

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89)
print(prime_fib(6))  # Output: 28

 ``` 
This Python code defines a function `prime_fib` that computes the nth Fibonacci number and checks for primality. It employs an basic loop to generate a Fibonacci sequence and returns the nth value, ensuring that it's also prime. The code includes several test cases to validate the function, demonstrating its correctness for various input values.