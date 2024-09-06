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

The function `is_prime` takes a number `n` as input and returns `True` if `n` is a prime, and `False` otherwise. It uses a various checks to determine if a number is prime:
- If `n` is less than or equal to 1, it is not prime.
- If `n` is less than or equal to 3, it is prime.
- If `n` is even or can be expressed as the product of two numbers less than 3, it is not prime.
- The function then uses a `while` loop to check if `n` is divisible by any number from 5 to the square root of `n`.

This function is self-contained and passes all the tests provided. It can be used as a core function to determine if a given number is prime or not.