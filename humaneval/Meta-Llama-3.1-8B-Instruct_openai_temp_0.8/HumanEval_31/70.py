### Prime Number Checker Script

Here's a Python script that checks if a given number is prime.

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):
        # Check divisors up to the square root of n
        if n % i == 0:
            # If n is divisible by any number, it's not prime
            return False
    return True


# Test cases
if __name__ == "__main__":
    print(is_prime(6))  # False
    print(is_prime(101))  # True
    print(is_prime(11))  # True
    print(is_prime(13441))  # True
    print(is_prime(61))  # True
    print(is_prime(4))  # False
    print(is_prime(1))  # False
```

### How it Works:

1. The `is_prime` function checks if a number `n` is prime by seeing if it has any divisors other than 1 and itself.
2. If `n` is less than or equal to 1, it immediately returns `False`, as these numbers are not prime.
3. The function then checks for divisors from 2 to the square root of `n` (inclusive).
4. If `n` is divisible by any of these numbers, it's not prime and the function returns `False`.
5. If `n` passes this test, it's prime and the function returns `True`.
6. The script includes test cases to demonstrate the function's usage and expected behavior.