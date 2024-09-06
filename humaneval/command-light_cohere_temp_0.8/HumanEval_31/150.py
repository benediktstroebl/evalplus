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
This script defines a function called `is_prime` that checks whether a given number is prime or not. The function uses basic primality tests, such as divisibility by 2 and 3, as well as checking divisibility by numbers that are the sum of two squares less than or equal to the given number. The function also checks for larger prime numbers by incrementing the value of `i` by 6 and testing for divisibility by numbers that are the sum of two squares of consecutive odd values of `i`. It then returns `True` if the given number is prime, and `False` otherwise.