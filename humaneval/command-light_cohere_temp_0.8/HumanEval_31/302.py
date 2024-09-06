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

# Test the function with some examples
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This script defines a function named `is_prime` that checks whether a given number is prime or not. The function employs a standard primality criteria, such as divisibility by 2 and 3, as well as the divisibility test by numbers forming the cube root of the given number. It also includes a specific case where n is 1, in which the function returns False by default. 

The test code demonstrates the function's behavior with a variety of input numbers and produces the anticipated results.