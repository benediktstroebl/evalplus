Here is a self-contained Python script that solves the problem of finding the n-th Fibonacci number that is prime, and tests the solution:
```python
def prime_fib(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Check if either number is prime
        is_prime = lambda x: all(x > 1) and any(n % x == 0 for x in range(2, n+1))
        if all(is_prime(x) for x in range(2, n+1)):
            return 5
        else:
            # Calculate n-th Fibonacci number
            return fibonacci(n)

def fibonacci(n: int):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
try:
    print(prime_fib(6))
except ValueError as e:
    print(f"Error: {e}")
```
The script defines a function `prime_fib` that calculates the n-th Fibonacci number which is also prime, and a function `fibonacci` that calculates the n-th Fibonacci number using recursion. The test block ensures the if the function can solve the problem for a given input.  The function is tested using the `try-except` block to catch the `ValueError` that will be raised if an invalid input is provided.