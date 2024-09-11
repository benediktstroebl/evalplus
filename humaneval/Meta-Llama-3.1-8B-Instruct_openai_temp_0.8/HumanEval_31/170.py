### Prime Number Checker
#### A Python Script to Check if a Number is Prime
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Only need to check up to sqrt(n)
        if n % i == 0:  # If n is divisible by any number, it's not prime
            return False
    return True  # If no divisors are found, the number is prime

if __name__ == "__main__":
    # Test cases
    print(is_prime(6))  # False
    print(is_prime(101))  # True
    print(is_prime(11))  # True
    print(is_prime(13441))  # True
    print(is_prime(61))  # True
    print(is_prime(4))  # False
    print(is_prime(1))  # False
```
This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It returns `True` if the number is prime and `False` otherwise. The function uses a simple iterative approach to check for primality, only checking up to the square root of `n` for divisors. The script also includes test cases to verify the correctness of the function.