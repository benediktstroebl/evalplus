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
The code defines a function `is_prime` that checks whether a given number is prime or not. The function first handles small numbers and returns `True` if the number is prime. The function then uses a `dividing` technique to test for primality, iterating up to the square root of the number while checking for divisibility. Finally, the function returns `False` if the number is not prime, indicating that it is not prime, and `True` if it is prime, indicating that it is a prime number.