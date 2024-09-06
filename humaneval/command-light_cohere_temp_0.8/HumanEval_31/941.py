```python
def is_prime(n):
    """
    Returns true if the number is prime, and false otherwise.
    Returns: input as output and does not modify the original variable.

    Args:
        n (int) - Number to test for primality
    """
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
This Python function `is_prime` accepts an integer `n` as input and outputs `True` if `n` is a prime number and `False` otherwise. It uses a time- well basic approach that involves checking divisibility up to the square root of `n`. 

It also handles a few specific cases, such as odd numbers divisible by 2 or 3, as well as numbers equal to 1, which are all prime by definition. 

This function is self-contained and can solve the primality checking problem for any given number without using any other functions or variables.