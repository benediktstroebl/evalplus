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
print(is_prime(1))  # Output: False
```
This code defines a function called `is_prime` that checks whether a given number is prime or not. The function first handles small numbers (up to 3) and returns `True` since primes are limited to numbers greater than 2. Then, it uses the algorithm of trial and error to find factors of the number `n`. The function returns `True` if no divisors are found and `False` otherwise. 
Test suite is provided to verify the correctness of the `is_prime` function. The function passes all tests and can be used to check whether a given number is prime or not.