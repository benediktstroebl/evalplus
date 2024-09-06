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
This code defines a function called is_prime that checks whether a given number is prime or not. The function uses a algorithm of trial and error, where it tries to divide the number by integers up to the square root, and returns True if the number is not divisible by any of these integers, indicating that it is prime. The function also handles the small odd prime numbers, as well as numbers that are divisible by 2 and 3, by checking divisibility only up to their square root.

The function passes all the tests with the given inputs.