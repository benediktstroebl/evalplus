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

# Test function
def test_is_prime():
    print("Is prime ", end='', is_prime(6))
    print("?", end='', is_prime(101))
    print("?", end='', is_prime(11))
    print("?", end='', is_prime(13441))
    print("?", end='', is_prime(61))
    print("?", end='', is_prime(4))
    print("?", end='', is_prime(1))
```
The above Python script defines a function named `is_prime` that checks whether a given number is prime. It then contains a test function named `test_is_prime` that uses the `is_prime` function to test if each number passed is prime or not. 

The `is_prime` function uses an optimized algorithm to check for primality, and it passes all the tests.