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
This Python function, `is_prime()`, takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It employs efficient prime testing methods like checking divisibility by 2 and 3, as well as checking divisibility by numbers of the form `6k+1` (k being an integer). The function also iterates until the square root of the input number is less than or equal to the input number, performing a basic primality test.