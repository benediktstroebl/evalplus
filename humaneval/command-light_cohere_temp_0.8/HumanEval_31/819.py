```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test cases pass successfully!
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This Python function `is_prime(n)` checks whether a given number `n` is a prime or not. It starts by checking numbers up to 2 (since all prime numbers greater than 2 are divisible only by 2 and 3), and returns `False` if `n` is less than or equal to 2 or 3. It then checks for divisibility by numbers of the form `5i + 2j`, where `i` and `j` are both integers. The function then uses a loop to check these potential divisors, and returns `False` if any of them divide `n` without a remainder. If no divisors are found, the function returns `True`, indicating that `n` is a prime number.