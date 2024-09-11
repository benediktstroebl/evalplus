### Prime Number Checker
#### A Python function to determine if a given number is prime.

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example use cases
if __name__ == "__main__":
    print(is_prime(6))       # False
    print(is_prime(101))     # True
    print(is_prime(11))      # True
    print(is_prime(13441))   # True
    print(is_prime(61))      # True
    print(is_prime(4))       # False
    print(is_prime(1))       # False
```

This function works by checking if the input number `n` is divisible by any number up to its square root. If it is, then `n` is not prime, and the function returns `False`. If no such divisor is found, then `n` is prime, and the function returns `True`. This approach is more efficient than checking all the way up to `n`, as it stops as soon as it finds a divisor.