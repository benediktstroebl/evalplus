```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters:
    n (int): The number to test for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to the square root of n
        if n % i == 0:  # If n is divisible by any number, it's not prime
            return False
    return True

# Test cases
if is_prime(6):
    print("Expected is_prime(6) to return False, but got True")
else:
    print("Correctly identified 6 as not prime")

if is_prime(101):
    print("Correctly identified 101 as prime")
else:
    print("Expected is_prime(101) to return True, but got False")

if is_prime(11):
    print("Correctly identified 11 as prime")
else:
    print("Expected is_prime(11) to return True, but got False")

if is_prime(13441):
    print("Correctly identified 13441 as prime")
else:
    print("Expected is_prime(13441) to return True, but got False")

if is_prime(61):
    print("Correctly identified 61 as prime")
else:
    print("Expected is_prime(61) to return True, but got False")

if is_prime(4):
    print("Expected is_prime(4) to return False, but got True")
else:
    print("Correctly identified 4 as not prime")

if is_prime(1):
    print("Expected is_prime(1) to return False, but got True")
else:
    print("Correctly identified 1 as not prime")
```

This Python script includes a function `is_prime` that checks whether a given number is prime or not. If the number is less than or equal to 1, it immediately returns `False` because prime numbers by definition are greater than 1. Then it iterates over all numbers from 2 up to the square root of `n` and checks if `n` is divisible by any of these numbers. If `n` is divisible, it means `n` is not a prime number and the function returns `False`. If the function finishes checking without finding any divisors, it means `n` is a prime number and it returns `True`.

The script also includes test cases to verify that the `is_prime` function is working correctly. 

This solution has a time complexity of O(√n), which is more efficient than checking every number up to n, which would have a time complexity of O(n). This is because a larger factor of n must be a multiple of a smaller factor that has already been checked.