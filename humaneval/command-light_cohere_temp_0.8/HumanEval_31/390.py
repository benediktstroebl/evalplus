Here is a self-contained Python function that checks whether a given number is a prime, with tests:
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
This function checks the given number `n` for primality. It uses a particular test of numbers less than 5, then checks divisibility by 2 and 3, and finally, it uses an optimized algorithm that uses squares of consecutive primes to test for primality. 

It is important to note that the function assumes that the input `n` is an integer, as the primality-checking algorithm involves integer numbers.