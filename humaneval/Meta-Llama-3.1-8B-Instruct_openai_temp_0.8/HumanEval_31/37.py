Here's a Python script that defines the `is_prime` function according to the specifications:
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    :param n: The number to check for primality.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This script checks whether a given number is prime by testing divisibility up to the square root of the number. If the number is divisible by any of these values, it is not prime. Otherwise, it is prime.