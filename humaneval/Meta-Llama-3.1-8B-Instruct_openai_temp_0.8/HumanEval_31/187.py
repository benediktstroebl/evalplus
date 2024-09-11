### Prime Number Checker
#### A Python Function to Determine Prime Numbers

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
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # Only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # Check odd numbers up to the square root
        if n % d == 0:
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

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It uses a simple algorithm to check for primality, only checking up to the square root of `n` to determine if it has any divisors other than 1 and itself. The function includes test cases to verify its correctness.