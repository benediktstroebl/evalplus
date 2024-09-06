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

# Test the function with some values
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This function is_prime(n) that accepts an integer n and returns True if n is a prime, and False otherwise. The function first checks if n is less than or equal to 1, and returns False in such cases. The function then checks for divisibility by 2 and 3, and returns False if n is divisible by either of these numbers. The function then iterates through i = 5, and checks if n is divisible by i or i + 2, and returns False if it is, and True if it isn't. If the condition holds for any of these values, the function returns True. If the function returns any of these tests, it correctly identifies the values that are prime.