### Prime Number Checker
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
    if n <= 1:  # numbers less than or equal to 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # if the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # we only need to check up to the square root of the number
        if n % i == 0 or n % (i + 2) == 0:  # check for divisibility by 6k - 1 and 6k + 1
            return False
        i += 6
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441)) # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It uses a simple algorithm that checks for divisibility by 2, 3, and then by all odd numbers up to the square root of `n`. If `n` is not divisible by any of these numbers, it is considered prime. The script includes test cases to verify the correctness of the `is_prime(n)` function.