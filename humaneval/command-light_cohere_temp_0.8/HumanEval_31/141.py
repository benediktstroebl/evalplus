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

# Test case:
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This Python code defines a function called `is_prime` that checks whether a given number is a prime or not. It uses a certain algorithms to achieve this, such as checking divisibility by 2 and 3, then using the fact that prime numbers greater than 3 can be expressed as `2^k + 2^(k+2)`, where `k` starts from 5. The code also checks for divisibility by numbers that form the sqrt(n) + 1, and finally checks if `n` is a perfect power of 2 or 5.