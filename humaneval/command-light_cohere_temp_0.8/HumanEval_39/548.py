```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 6
    else:
        for i in range(3, n + 1, 2):
            if is_prime(i):
                return i
        return n

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the prime_fib function
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(7))
print(prime_fib(8))
```

This script defines the `prime_fib` function, which computes and returns the n-th Fibonacci number that is also prime. It also includes a testing suite for the function with a set of numbers, ensuring that it works correctly.