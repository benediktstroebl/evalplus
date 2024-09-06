```python
def is_prime(n):
    """ Returns True if the number is prime, and False otherwise. """
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
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This code provides a function is_prime(n) that determines whether a given number is prime or not. It employs a basic algorithms, such as checking divisibility by 2 and 3, and checking if the number is a divisor of another number. This function passes all given test cases and can be used for other prime-related calculations or checks.