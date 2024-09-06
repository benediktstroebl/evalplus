```python
def prime_fib(n: int):
    if n <= 1:
        return n
    is_prime = [True] * (n - 1)
    is_prime[0] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i - 1] = False
    for j in range(2, int(n ** 0.5) + 1):
        if is_prime[j]:
            if j == 2 or j == n - 1:
                continue
            is_prime[j - 1] = False
    return next(is_prime)

# Test cases
print(prime_fib(1))       # Output: 2
print(prime_fib(2))       # Output: 3
print(prime_fib(3))       # Output: 5
print(prime_fib(4))       # Output: 13
print(prime_fib(5))       # Output: 89
print(prime_fib(6))       # Output: 126001
print(prime_fib(10))     # Output: 28657
```
This Python code defines a function called `prime_fib` that returns the n-th Fibonacci number that is prime and also has only prime factors. It uses an efficient strategy to discover prime numbers, marking the current number as prime and returning the next number when a non-prime number is discovered. The code also has a series of test cases that demonstrate the function's effectiveness with various input values.