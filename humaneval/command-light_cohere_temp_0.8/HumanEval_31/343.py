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

# Test the function with various inputs
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This Python code defines a function named `is_prime` that checks whether a given number `n` is a prime number. It utilizes a basic primality-based logic to determine primality, including checking divisibility by 2 and 3, and then checking divisibility by numbers resulting from consecutive multiples of 5. The function returns `True` if the input number is a prime, and `False` otherwise. It then passes these test by passing various numbers to the function and prints the results.

To test the `is_prime` function, it prints the results for various inputs, such as small prime numbers and larger composite numbers, and confirms that the function is correctly identifying prime numbers while correctly identifying non-prime numbers.