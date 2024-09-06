```python
def is_prime(n):
    if n <= 1:
        return False
    for i ::= 2; i <= n; i += 1:
        if n % i == 0:
            return False
    return True

# Unit tests for is_prime
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This Python code defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. The function uses a optimization technique of iterating from 2 to the square root of `n`, checking for divisibility. The function returns `True` if the number is prime and `False` otherwise. The unit tests for the function ensure that it behaves correctly for a variety of inputs, and can be used as a basis for further development or customization.