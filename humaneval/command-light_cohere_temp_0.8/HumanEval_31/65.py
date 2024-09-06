```python
def is_prime(n):
    """Returns true if the number is prime, and false otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True

# Test the function with some inputs
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The function `is_prime` returns true if the number is prime, and false otherwise. The function uses a basic algorithm to check if a number is prime or not. The function iterates from 2 to the square root of the number and checks if the number divided by any number in this range is equal to 0.