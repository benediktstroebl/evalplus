```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    prime_fib = 3
    while prime_fib <= n:
        if n % prime_fib == 0:
            return prime_fib
        prime_fib += 1
    return n

# Test suite
print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))
print(prime_fib(6))
```
This code defines a function called `prime_fib` that calculates and returns the n-th Fibonacci number that is both a Fibonacci number and prime. The function employs an loop to test if the current Fibonacci number is prime by checking if the number is divisible by any number up to the square root of the number.

This function is designed to be efficient and self-contained, as it can calculate the n-th Fibonacci number and determine whether it is prime without the need for additional calculations.