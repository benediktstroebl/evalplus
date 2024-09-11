### Prime Number Checker
#### Problem Description

The following Python script is a self-contained program that checks if a given number is prime.

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

    Args:
    n (int): The number to be checked for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:
        # 2 is the only even prime number
        return True
    if n % 2 == 0:
        # All other even numbers are not prime
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
if __name__ == "__main__":
    print(is_prime(6))   # False
    print(is_prime(101)) # True
    print(is_prime(11))  # True
    print(is_prime(13441)) # True
    print(is_prime(61))  # True
    print(is_prime(4))   # False
    print(is_prime(1))   # False
```

This script uses a helper function `is_prime(n)` to check if a given number `n` is prime. It first handles the edge cases where `n` is less than or equal to 1, or where `n` is 2 (the only even prime number). It then checks odd factors of `n` up to the square root of `n` using a loop.

The test cases at the end of the script demonstrate the function's correctness by printing `True` for prime numbers and `False` for non-prime numbers.