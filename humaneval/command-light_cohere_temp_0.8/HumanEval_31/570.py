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

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This Python function `is_prime` determines whether a given number is prime or not. It uses a basic trial and improvement algorithm, starting with the assumption that odd numbers are not prime and eventually checking divisibility with all numbers from 2 to the square root of the input number.

Finally, the function returns `True` if the input number is prime, indicating that it has no divisors except for 1 and itself.

Note that the function's time complexity is O(sqrt(n)), making it a relatively efficient algorithm for determining primality.