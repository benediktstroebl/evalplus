```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if is_prime(a):
            a, b = next(b for b in list(range(a + 1)) if is_prime(b))
    return b

def is_prime(n: int):
    if n <= 1:
        return False
    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            return False
    return True

# Test the prime_fib function
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(7))
print(prime_fib(8))
```
This Python script defines a function `prime_fib` that computes the n-th Fibonacci number that is prime and returns the corresponding value. It also includes a function `is_prime` that checks if a given number is prime or not. The script then tests the function `prime_fib` using the test suite and prints the results.

Note: this script is self-contained and doesn't require external modules or functions.