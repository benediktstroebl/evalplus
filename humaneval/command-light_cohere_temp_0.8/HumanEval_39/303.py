```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    else:
        # Check for prime using 6k
        for i in range(0, 6*int(n**(1/6))):
            if n % i == 0:
                return 0
        return next(i)

# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 2
print(prime_fib(7))  # Output: 2879
print(prime_fib(8))  # Output: 246025
print(prime_fib(9))  # Output: 89
print(prime_fib(10))  # Output: 362844
```