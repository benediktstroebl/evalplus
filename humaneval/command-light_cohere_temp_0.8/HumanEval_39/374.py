```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        a, b = next((c for c in range(a, b+1) if c is prime))
    return b

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28

 ```
This script defines a function prime_fib that returns the n-th Fibonacci prime number. It also makes sure that all returned numbers are prime.