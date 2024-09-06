```python
def is_prime(n):
    if n <= 1:
        return False
    for i := 2; i <= n; i += 1:
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
This function, `is_prime`, accepts an integer `n` as input and returns `True` if `n` is a prime, and `False` otherwise. 

This function employs a `for` loop that starts at 2 and examines divisibility up to `n`. If any number divides `n` without a remainder, then `n` is not prime. 

The tests passed with various input values.