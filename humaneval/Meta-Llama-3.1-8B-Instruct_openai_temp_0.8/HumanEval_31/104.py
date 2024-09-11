### Prime Number Checker
#### A Python Script to Check if a Number is Prime

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Corner cases: numbers less than 2 are not prime
    if n < 2:
        return False

    # Check divisibility up to the square root of n
    # This is because a larger factor of n must be a multiple of a smaller factor that has already been checked
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    # If no divisors are found, the number is prime
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. The function uses a simple trial division method, checking for divisibility up to the square root of `n`. If no divisors are found, the number is considered prime. The script also includes test cases to verify the correctness of the `is_prime(n)` function.