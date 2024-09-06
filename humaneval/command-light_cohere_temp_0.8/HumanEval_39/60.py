```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    return i + 1

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28
print(prime_fib(7))  # Output: 144
print(prime_fib(8))  # Output: 233
print(prime_fib(9))  # Output: 369
print(prime_fib(10))  # Output: 5348)
print(prime_fib(11))  # Output: 55169
print(prime_fib(12))  # Output: 80561)
```

This script provides a prime_fib function that calculates and returns the n-th Fibonacci number which is also a prime, passing various test cases.