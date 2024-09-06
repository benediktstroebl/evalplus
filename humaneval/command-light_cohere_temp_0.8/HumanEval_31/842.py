Here's a Python script with a self-contained function that solves the problem and passes the tests provided:

```python
def is_prime(n):
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

# Unit tests
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This code defines a `is_prime` function that determines whether a given number is a prime. The function initially determines whether the numbers are less than or equal to 1, in which case they are not prime. It then determines if the numbers are less than or equal to 3, in which case they are prime. The function then checks for divisibility by 2 and 3, returning `False` if the number is divisible by either of these. It then starts a loop that checks for divisibility by consecutive odd numbers, starting from 5. If the number is divisible by any of these odd numbers, it returns `False`, indicating that the number is not prime. If the loop completes without finding a divisor, it returns `True`, indicating that the number is prime.

This function is then tested with a series of input numbers, and the output is printed to the console. The function correctly identifies whether each number is prime or not, and passes all the tests.