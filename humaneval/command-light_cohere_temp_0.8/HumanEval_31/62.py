```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
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

This Python function `is_prime` takes a number `n` as input and checks whether it's a prime number. It iterates from the basic primality tests, such as 2, 3, and 5 (which are prime numbers), as well as the square and square root of the number. The function returns `True` if the number is prime and `False` if it's not. 

Please note that this function can be used to check whether a given number is a prime or not. It can also be used to perform various mathematical operations.