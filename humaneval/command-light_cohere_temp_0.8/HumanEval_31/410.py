Here is a Python script with a self-contained function that solves the is_prime problem and passes the tests:
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

# Test suite
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False)
```
The code defines a function `is_prime` that checks whether a given number is prime or not. The function first handles the smaller prime numbers, then checks divisibility by 2 and 3, and finally uses a loop to check divisibility by consecutive primes up to the square root of the number. The function returns True if the prime, and False otherwise.