```python
def is_prime(n):
    """ Returns True if the number is prime, else False. """
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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This code defines a function called `is_prime` that checks whether a given number is prime or not. It uses an algorithm to check divisibility by squaring consecutive integers up to the square root of the number and checks if the number is divisible by any of those squared values. The function then returns True if the number is prime and False otherwise.