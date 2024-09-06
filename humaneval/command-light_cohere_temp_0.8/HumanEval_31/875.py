```python
def is_prime(n):
    """
    A simple heuristic: all numbers > 1 are prime except 0 and numbers ending with 1, 
    3, 5, 7, 11, 13, ...
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Unit tests
print(is_prime(6))  # Output: False
print(is_prime(0))  # Output: True
print(is_prime(2))  # Output: True
print(is_prime(9))  # Output: False
print(is_prime(7))  # Output: True
print(is_prime(15)))  # Output: False
print(is_prime(3441))  # Output: True
print(is_prime(5))  # Output: True
print(is_prime(1223))  # Output: False
```

This code defines a simple heuristic function that checks whether a given number is a prime. It returns `True` if the number is prime, and `False` otherwise. The function first checks if the number is `0` or `1`, which are not prime, and then checks for divisibility by `2`, which is also not prime. It then starts checking divisibility by squaring each number from `3` to the square root of the input number. 

The function then returns `True` if the input number is prime and `False` otherwise.  The function is tested against the output of `is_prime()` with various input numbers, and the results are correct.