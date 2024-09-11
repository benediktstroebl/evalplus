```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:  # Prime numbers are greater than 1
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    sqrt_n = int(n**0.5) + 1  # Only need to check up to the square root
    for i in range(3, sqrt_n, 2):  # Check odd numbers only
        if n % i == 0:  # If divisible by any number, not prime
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

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It uses a few checks to optimize the process:

1.  If `n` is less than or equal to 1, it is not prime.
2.  If `n` is 2, it is prime.
3.  If `n` is an even number (except for 2), it is not prime.
4.  It checks divisibility up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root.
5.  It checks for odd factors only, as even factors have already been accounted for.

The script includes the test cases from the problem statement to demonstrate the function's correctness.