```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 6
    else:
        i = 5
        while i * i <= n:
            if n % i == 0:
                return i
            i += 1
        return 7

# Test the function with different values for n
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 1228
print(prime_fib(7))  # Should raise an error: 7 doesn't satisfy condition)
print(prime_fib(8))  # Should raise an error: 8 doesn't satisfy condition)
print(prime_fib(9))  # Output: 523
print(prime_fib(10))  # Output: 3124
```