### Primality Test Function
```markdown
### Description
This script defines a function `is_prime(n)` that checks if a given integer `n` is prime.

### Code
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # all other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # check odd divisors only
        if n % d == 0:
            return False
    return True
```

### Example Usage
```python
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This script uses a simple trial division method to check for primality, which is sufficient for small to medium-sized integers. For larger integers, a more efficient approach may be needed, such as the Miller-Rabin primality test.