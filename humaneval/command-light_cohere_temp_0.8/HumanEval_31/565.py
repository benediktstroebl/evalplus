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
This function, `is_prime`, checks whether a given number is prime or not. It iterates from 2 to the square root of the number and checks for divisibility. If the number fails any test at any point, it returns `False`, indicating that the number is not prime. If the loop completes without finding a divisor, it returns `True`, indicating that the number is prime.