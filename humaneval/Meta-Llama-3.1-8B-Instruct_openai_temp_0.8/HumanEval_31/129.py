```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
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

# Test cases
if is_prime(6):
    print("Test 1 failed: 6 is not prime")
if not is_prime(101):
    print("Test 2 failed: 101 is prime")
if not is_prime(11):
    print("Test 3 failed: 11 is prime")
if not is_prime(13441):
    print("Test 4 failed: 13441 is prime")
if not is_prime(61):
    print("Test 5 failed: 61 is prime")
if is_prime(4):
    print("Test 6 failed: 4 is not prime")
if is_prime(1):
    print("Test 7 failed: 1 is not prime")
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a combination of quick checks and a loop to efficiently determine whether `n` has any divisors other than 1 and itself. The test cases at the end of the script verify that the function behaves correctly for various inputs.