Here is a Python script that solves the problem and passes the corresponding tests:
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
    print("Is prime(6):", is_prime(6), end=" ")
    print("Is prime(101):", is_prime(101), end=" ")
    print("Is prime(11):", is_prime(11), end=" ")
    print("Is prime(13441):", is_prime(13441), end=" ")
    print("Is prime(61):", is_prime(61), end=" ")
    print("Is prime(4):", is_prime(4), end=" ")
    print("Is prime(1):", is_prime(1), end=" ")

# Usage
test_is_prime()
```

This script defines a function `is_prime` that checks whether a given number is prime. It then provides a specific test cases using the `test_is_prime` function to verify the correctness of the `is_prime` function. 

Note: This implementation uses a `while` loop and basic factorization to check for primality.  The script also utilizes the `print` function to display the test results.