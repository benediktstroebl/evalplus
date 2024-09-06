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

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The provided Python code defines a function called `is_prime` that checks whether a given number is a prime or not. It first handles the Services from the `n <= 1` to return `False` as non-prime, and then checks for other prime numbers by looking for factors and divisors that are less than or equal to the square of `i` which starts at 5 and increases by 6 each time until the square of `i` is less than or equal to the given number. The function returns `True` if no divisors are found.