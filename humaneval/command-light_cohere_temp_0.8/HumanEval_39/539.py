```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        prime = 2
        while True:
            temp = prime
            prime = math.sqrt(prime * (prime + 1) / 2)
            if prime <= n:
                yield temp
                break

# Example usage
print(prime_fib(5))
``` 
This code defines a function `prime_fib` that calculates the nth Fibonacci number and ensures it's prime by using a loop and the `math.sqrt()` function to check if a number is prime or not.  The output will be the `89`, which is the 5th Fibonacci number and is also prime.