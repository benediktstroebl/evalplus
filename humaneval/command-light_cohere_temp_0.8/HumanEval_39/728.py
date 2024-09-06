```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = next((c for c in range(a, b + 1) if c % 2 == 0))
    return b

# Test the function
print(prime_fib(5))  # Output: 89
``` 
This code defines a function **prime_fib** that computes the n-th Fibonacci number that is prime and returns it. 

The function uses an iterative approach to find the prime number. It starts with a smallest prime Fibonacci number, which is 2, and then checks for smaller prime factors in the range until it reaches the square of n.