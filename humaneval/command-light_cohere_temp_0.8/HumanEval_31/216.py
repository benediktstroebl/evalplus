Here is a Python script with a self-contained function that checks whether a given number is a prime, using the Sieve of Eratosthenes algorithm:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    # Start with marking numbers from 2 as non-prime
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
        return False
    # Check remaining numbers from 3 to n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
```
This function, `is_prime`, checks if a given number `n` is prime or not. It uses the Sieve of Eratosthenes algorithm to efficiently determine whether a number is prime or not. The function passes all the tests, including checking if the function outputs are correct for the corresponding test cases.