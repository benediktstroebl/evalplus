```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:  # numbers less than or equal to 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # all other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # check odd numbers only
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

This script uses a helper function that checks for primality. It first handles edge cases (numbers less than or equal to 1 and the number 2). It then checks if the number is even (in which case it's not prime). Finally, it checks for odd divisors up to the square root of the number. If it finds any divisors, it returns False; otherwise, it returns True.