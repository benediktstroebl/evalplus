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

This script defines a function named is_prime that checks whether a given number n is prime or not. The function first handles some base cases: numbers less than or equal to 1, and numbers divisible by 2 or 3 are not prime. Then, it iterates up to the square of the input number while checking for divisibility by consecutive odd numbers (up to the square root of the input number). This ensures an efficient and efficient prime-checking.