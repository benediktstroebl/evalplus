```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None

    # Initialize first two fibonacci numbers
    a, b = 0, 1
    count = 0

    while True:
        # Generate next fibonacci number
        c = a + b
        count += 1

        # Check if the generated number is prime
        if is_prime(c):
            if count == n:
                return c
        a, b = b, c

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a `prime_fib` function that generates Fibonacci numbers until it finds one that is prime, starting the sequence over once the count of primes exceeds the desired `n` input. It also includes a `is_prime` function that checks if a number is prime using a standard algorithm. This is used to validate the output of `prime_fib` against known values. 
 unsurpassedContestions are welcomed to test and verify this code. Feel free to adapt it to your needs. If you have any questions or need further assistance, let me know!