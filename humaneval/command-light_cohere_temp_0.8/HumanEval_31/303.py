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

This Python function is_prime checks whether a given number is a prime or not. It employs various criteria and algorithms to determine whether a number is prime, such as checking divisibility by 2, 3, and other small primes up to the square root of the number. The function also checks for numbers less than or equal to 1, as they are not prime, and then finally it checks divisibility by numbers that are at least 5 times larger than the original number.