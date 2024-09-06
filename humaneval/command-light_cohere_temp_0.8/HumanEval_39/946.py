```python
import math

def is_prime(n):
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

def prime_fib(n):
    if n <= 0:
        return None
    
    if n == 1:
        return 2
    if n == 2:
        return 3
    
    # A fast prime initialization
    fast_primes = [2, 3]
    
    fib_sequence = [fast_primes[-1]]
    
    for num in range(3, n + 2):
        if is_prime(num):
            fib_sequence.append(num)
        fast_primes.append(num)
    
    return fib_sequence[-1]

# Example usage
print(prime_fib(5))
``` 
This code defines the function `prime_fib` which calculates the n-th Fibonacci number that is also prime. The function first checks if n is less than or equal to 1, in which case it returns False. It then checks for small divisors of n, including 2 and 3, and returns True if n is not divisible by those numbers. The function then initializes a list `fast_primes` with the prime numbers 2 and 3. It then uses a loop to generate the Fibonacci sequence by iterating from 3 to n+1. The function then returns the last element of the Fibonacci sequence, which represents the n-th Fibonacci number that is also prime.