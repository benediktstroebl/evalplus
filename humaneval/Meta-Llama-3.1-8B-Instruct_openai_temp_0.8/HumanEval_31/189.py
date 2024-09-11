### Prime Number Checker
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

    A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
    """
    if n <= 1:  # Prime numbers are greater than 1
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to the square root of n
        if n % i == 0:  # If n is divisible by i, it's not a prime number
            return False
    return True  # If no divisors are found, n is a prime number

# Test cases
print(is_prime(6))     # False
print(is_prime(101))   # True
print(is_prime(11))    # True
print(is_prime(13441)) # True
print(is_prime(61))    # True
print(is_prime(4))     # False
print(is_prime(1))     # False
```
This script defines the `is_prime` function, which checks if a given number is prime or not. It uses a simple trial division method to find divisors up to the square root of the number. If no divisors are found, the number is prime and the function returns `True`. Otherwise, it returns `False`. The test cases at the end verify the correctness of the function.