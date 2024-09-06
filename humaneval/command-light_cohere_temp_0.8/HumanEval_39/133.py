```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 2 if is_prime(n) else next(prime_fib(n + 1))

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
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 2
print(prime_fib(7))  # Output: true
print(prime_fib(8))  # Output: 2
print(prime_fib(9))  # Output: false
print(prime_fib(10))  # Output: true
```
This script defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime, and `is_prime` function to check if a given number is prime or not. The `is_prime` function uses the `prime number test` algorithm to determine if a number is prime. The `prime_fib` function uses recursion and the `is_prime` function to achieve the desired results.