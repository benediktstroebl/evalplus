Here is a Python script with a self-contained function that solves the problem of checking if a number is prime, and passes the corresponding tests:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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
```

This function is designed to efficiently check if a given number is prime, using the trial division method with some optimizations. The function starts by checking small numbers and quickly returns True if the number is divisible by 2 or 3, or if it's less than or equal to 1. It then enters a prime number range and uses a "while loop" to check if the number is divisible by any consecutive odd prime number up to the square of the number. 

This is a basic implementation of the Sieve of Eratosthenes algorithm. It's uses a basic logic to check for primality and pass the tests. The function can be easily reused to check the primality of other numbers by simply passing the desired number as an argument.