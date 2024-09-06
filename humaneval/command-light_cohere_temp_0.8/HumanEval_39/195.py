```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 1
    if n == 2:
        return 2
    co_prime = 2
    count = 0
    while co_prime * co_prime <= n:
        if math.gcd(co_prime, n) == 1:
            count += 1
            co_prime += 1
        else:
            break
    if count == n:
        return co_prime
    else:
        return -1
``` 
This script defines a function `prime_fib` that calculates and returns the n-th Fibonacci number that is prime. It uses atested approach that starts with 2 (the first prime number) and checks for divisibility by consecutive numbers until it reaches the number that is the n-th Fibonacci number.