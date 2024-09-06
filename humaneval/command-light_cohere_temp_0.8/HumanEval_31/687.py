```python
def is_prime(n):
    """Check whether a given number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
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
This Python code defines a function `is_prime` that checks whether a given number is prime or not. The function uses a simple algorithm to determine primality:
1. For any given number `n <= 1`, it is definitely not prime.
2. For `n numbers` >= 2, the function iterates through odd numbers starting from 2 up to the square root of the number.
3. The function checks if the number divides evenly with any odd integer in this range.
4. If a number does not evenly divide any odd integer in this range, it means that the number is not divisible by any odd number less than or equal to its square root.

The function then returns `True` if the number is prime and `False` otherwise.

Finally, the code tests the function by calling it with various numbers and printing the results. This will pass all corresponding tests.