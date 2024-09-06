```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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
This function, `is_prime`, accepts an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. 

The function employs a combination of conditions to determine whether `n` is prime. It begins by evaluating whether `n` is less than or equal to 1, in which case it returns `False` since prime numbers are greater than 1. Then, it checks if `n` is less than or equal to 3, in which case it returns `True` since all prime numbers greater than 3 are also even numbers. The function then checks for divisibility by testing if `n` is divisible by 2 or 3, returning `False` if this condition is met. It then initializes a variable `i` to 5 and iterates until the square of `i` exceeds `n`. It then checks for divisibility by testing if `n` is divisible by `i` or `i + 2`, returning `False` if this condition is met. The function then returns `True` if no divisors are found.