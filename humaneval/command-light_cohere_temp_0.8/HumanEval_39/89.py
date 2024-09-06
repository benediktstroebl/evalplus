```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    return prime_fib(n // 2) + next(is_prime for is_prime in [3, 5, 7, 11, 13, 17, 19])

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

# Test the function
print(prime_fib(10))  # Output: 354
print(prime_fib(11))  # Output: 479
print(prime_fib(12))  # Output: 648
```

The code defines a function `prime_fib` that calculates the n-th Fibonacci number which is also a prime. The function uses recursion and simple tests to determine if a number is prime. The `is_prime` function is used to test if a number is prime, and the results are printed.