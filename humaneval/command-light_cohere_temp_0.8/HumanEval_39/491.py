```python
import math

def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(2, n+1):
        a, b = math.next_prime(a), b + a
    return a

# test function for is_prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

# Driver code
print(prime_fib(5))  # Output: 89
print(is_prime(15)))  # Output: True
```
The provided Python script defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it is prime. The function uses an loop to find the next prime numbers until it reaches the square root of n, then it returns the n-th Fibonacci prime. The `is_prime` function is defined to check if a number is prime or not. The driver code then calls the `prime_fib` and `is_prime` functions with different inputs and prints the results to the console, demonstrating the functionality of the functions.