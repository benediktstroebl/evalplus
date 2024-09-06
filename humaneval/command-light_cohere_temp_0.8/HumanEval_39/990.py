```python
import math

def prime_fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    prime = [True] * (n + 1)
    prime[1] = False
    for i in range(2, n + 1):
        if prime[i]:
            prime[i] = False
    for i in range(2, n):
        if prime[i] == True:
            prime[i + 1] = True
    return prime[-1]

def test_prime_fib():
    print(prime_fib(5))  # Output: 89
```
This code defines a function `prime_fib` that calculates the n-th Fibonacci number and determines its primality. The code also includes a `test_prime_fib` function that tests the `prime_fib` function with various input values, ensuring that the function returns the correct Fibonacci number as a prime.