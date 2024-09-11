```python
# Define a function to check if a number is prime
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    # Corner cases: non-positive numbers are not prime
    if n <= 1:
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

    # If no factors found, n is prime
    return True

# Example use cases
if __name__ == "__main__":
    print(is_prime(6))  # False
    print(is_prime(101))  # True
    print(is_prime(11))  # True
    print(is_prime(13441))  # True
    print(is_prime(61))  # True
    print(is_prime(4))  # False
    print(is_prime(1))  # False
```

This Python script defines a function `is_prime(n)` that checks whether a given integer `n` is prime or not. It uses a simple trial division method to test for primality, checking odd factors up to the square root of `n`. The function includes corner cases for non-positive numbers and the number 2, which is the only even prime number. The example use cases demonstrate the function's behavior with various inputs.