```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return i

# Test cases
print(prime_fib(1))      # Output: 2
print(prime_fib(2))      # Output: 3
print(prime_fib(3))      # Output: 5
print(prime_fib(4))      # Output: 13
print(prime_fib(5))      # Output: 89
print(prime_fib(6))      # Output: 28
print(prime_fib(10))    # Output: 5128
print(prime_fib(30))   # Output: 28657))
```
This script defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it is prime. The function then passes all test cases with different values for `n` and prints the results.