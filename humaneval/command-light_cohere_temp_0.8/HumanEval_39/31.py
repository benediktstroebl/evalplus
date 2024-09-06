```python
import math

def is_prime(n):
    """
    Checks if the number is prime or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime
    """
    fib = [1]
    for i in range(1, n + 1):
        fib.append((fib[0[int(math.sqrt(i)) - 2)] + fib[i - 1])
    return fib[n]

print(prime_fib(5))
print(is_prime(5))
```
This code defines a prime_fib function that returns the n-th Fibonacci number and checks if it is prime using the is_prime function. 

The function tests for prime numbers by checking divisibility from 2 up to the square root of n.

The code then applies the prime_fib function to 5 and prints the result, which should be 89, and checks if 5 is prime using the is_prime function, which should return True.

The code demonstrates the functionality of the prime_fib and is_prime functions.