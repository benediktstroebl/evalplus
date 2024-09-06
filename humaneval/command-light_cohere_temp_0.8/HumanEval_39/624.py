Here's a complete Python script with a self-contained function that calculates and returns the n-th Fibonacci number that is also prime:

```python
import math

def is_prime(n):
    """
    checks if an integer is prime by using the Sieve of Eratosthenes algorithm.
    small = [ [1, 2, 3]
    is_prime_list = [True] * (n + 1)
    is_prime_list[0] = is_prime_list[1] = False
    is_prime_list[2] = is_prime_list[3] = False
    for num in range(4, n + 1, 2):
        is_prime_list[num] = False
    for num in is_prime_list:
        if num and math.isPowerSet(num):
            continue
    for i in range(2, n + 1):
        if is_prime_list[i] and not is_prime_list[i - 1]:
            return False
    return True

def prime_fib(n: int):
    """
    returns n-th Fibonacci number that is prime
    """
    return is_prime(n)[is_prime(n - 1)]

print(prime_fib(5))
```
This code defines a function `is_prime` that checks if a number is prime using the Sieve of Eratosthenes algorithm. It also defines a a function `prime_fib` that calculates the n-th Fibonacci number and returns it if it is prime, otherwise it returns 0.  The function uses the `is_prime` to check if the current Fibonacci number is prime and then returns `is_prime(n - 1)` which is the next Fibonacci number.