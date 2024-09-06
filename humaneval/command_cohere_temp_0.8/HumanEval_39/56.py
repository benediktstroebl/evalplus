```python
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
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        prime_fib_prev = prime_fib(n - 1)
        if prime_fib_prev is None:
            return None
        prime_fib_curr = prime_fib(n - 2)
        if prime_fib_curr is None:
            return None
        return prime_fib_prev if is_prime(prime_fib_curr) else prime_fib_curr
```
The code defines two functions:
1. The `is_prime` function checks whether a given number is prime or not. It handles special cases like numbers less than or equal to 1, and handles known prime numbers like 2 and 3 differently. It then performs a linear probed trial division algorithm starting from 5 up to the square root of the number, incrementing by 6 each time, to efficiently determine if the number is prime. 
2. The `prime_fib` function is a recursive function that finds the n-th Fibonacci number that is also a prime number. The function starts with checking if n is within a valid range (n >= 1) and returns 2 if n is 1 as the first prime Fibonacci number. It returns 3 if n is 2 as the second prime Fibonacci number. For any other value of n, it recursively calls `prime_fib` for n-1 and n-2 to build up the Fibonacci sequence. It then checks if the current Fibonacci number is prime using the `is_prime` function. If it is prime, it returns it; otherwise, it returns the previous prime Fibonacci number.