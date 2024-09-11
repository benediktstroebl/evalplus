```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    if n <= 3:
        # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:
        # Numbers divisible by 2 or 3 are not prime
        return False
    i = 5
    while i * i <= n:
        # Check for divisibility up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            # Numbers divisible by any number in this range are not prime
            return False
        i += 6
    # If all checks pass, the number is prime
    return True

# Test cases
if is_prime(6):
    raise AssertionError("Expected is_prime(6) to return False")
if not is_prime(101):
    raise AssertionError("Expected is_prime(101) to return True")
if not is_prime(6):
    raise AssertionError("Expected is_prime(6) to return False")
if is_prime(101):
    raise AssertionError("Expected is_prime(101) to return True")
if is_prime(11):
    raise AssertionError("Expected is_prime(11) to return True")
if is_prime(13441):
    raise AssertionError("Expected is_prime(13441) to return True")
if is_prime(61):
    raise AssertionError("Expected is_prime(61) to return True")
if is_prime(4):
    raise AssertionError("Expected is_prime(4) to return False")
if is_prime(1):
    raise AssertionError("Expected is_prime(1) to return False")
print("All test cases pass")
```

This script defines a function `is_prime` that checks whether a given number is prime. It uses a combination of simple checks and a loop to efficiently determine primality. The test cases at the end of the script verify that the function works correctly.