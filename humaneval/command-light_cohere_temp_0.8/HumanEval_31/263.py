Here's a Python script that includes a self-contained function `is_prime`, which determines whether a given number is prime or not, and passes all the test cases:
```python
def is_prime(n):
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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This script defines a function called `is_prime` that determines whether a given number `n` is prime or not. The function first checks if `n` is less than or equal to 1, and returns `False` in such cases. Then, it checks for divisibility by 2 and 3, returning `False` if `n` is divisible by either of these numbers. The function then initializes a counter `i` to 5 and starts a while loop, checking if `n` is divisible by `i` or `i + 2`. The loop continues until the square of `i` is less than or equal to `n`.

The function then returns `True` if none of these conditions are met, indicating that `n` is a prime number. 

This function is self-contained, and it can be used to determine the primality of any given number.