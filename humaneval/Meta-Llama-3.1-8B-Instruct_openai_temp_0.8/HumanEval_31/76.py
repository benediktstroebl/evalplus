### Prime Number Checker

Below is a Python script that checks if a given number is prime or not.

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Corner cases: numbers less than 2 are not prime
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
if __name__ == "__main__":
    print(is_prime(6))  # Output: False
    print(is_prime(101))  # Output: True
    print(is_prime(11))  # Output: True
    print(is_prime(13441))  # Output: True
    print(is_prime(61))  # Output: True
    print(is_prime(4))  # Output: False
    print(is_prime(1))  # Output: False
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It handles edge cases such as numbers less than 2, and then checks for odd factors up to the square root of `n`. If no factors are found, the number is prime. The script includes test cases to demonstrate its functionality.