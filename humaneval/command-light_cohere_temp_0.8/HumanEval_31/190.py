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
The code defines a `is_prime` function that checks whether a given number is a prime. The function implements a standard primality testing logic, where it iterates up to the square root of the number while checking for divisibility with small prime numbers and odd multiples. The function returns `True` if the number is prime, and `False` otherwise. The function passes all these tests with various input values and prints the corresponding outputs, confirming the correctness of the primality-checking logic.