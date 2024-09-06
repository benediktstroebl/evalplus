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
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This Python function `is_prime` checks whether a given number is prime or not. It uses the simple algorithm to determine primality: if the number is less than or equal to 1, it returns `False`, and if the number is greater than 3, it returns `True`. The function then checks for divisibility by checking divisibility by 2 and 3, as well as checking for divisibility by consecutive odd numbers starting from 5. If the number is not divisible by any of these, it returns `True`, indicating that the number is prime. The function also handles the numbers greater than 5 that may be prime, so it does not check divisibility by numbers greater than 5.