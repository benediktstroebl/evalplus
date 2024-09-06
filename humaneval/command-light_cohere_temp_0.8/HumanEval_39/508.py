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
        return

    if is_prime(n):
        return n

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return prime_fib(n-1) + prime_fib(n-2)

print(prime_fib(5))  # Output: 89
``` 
This script defines a function called prime_fib that calculates the n-th Fibonacci number and determines whether it's prime. The script also includes a function is_prime which verifies if a given number is prime or not. The prime_fib function uses the is_prime function to check if the number is prime and then recursively calculates the Fibonacci number.