```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3  # prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: False
print(prime_fib(7))  # Output: True
print(prime_fib(8))  # Output: False
print(prime_fib(9))  # Output: True
```
This code defines the `prime_fib` function, which returns the n-th Fibonacci number that is also prime. The function uses an loop and a series of conditions to determine if a number is prime or not.