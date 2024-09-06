```python
def is_prime(n):
    """Returns true if the number is prime, and false otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True

#Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

The above Python code defines a function named `is_prime` that checks whether a given number is prime or not. It iterates through loop from 2 up to the square root of the number and checks if the number is divisible by any of these values. If it is, then it returns `False`, indicating that the number is not prime. If no of these values is divisible, it returns `True`, indicating that the number is prime. 

The function is then tested with various input values, and the output is printed to the console to verify its correctness.