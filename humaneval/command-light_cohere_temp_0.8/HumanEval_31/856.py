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

# Test function to check if a given number is prime
def is_prime_test(n):
    return is_prime(n)

# Test cases
print(is_prime_test(6))  # Output: False
print(is_prime_test(101))  # Output: True
print(is_prime_test(11))  # Output: True
print(is_prime_test(13441))  # Output: True
print(is_prime_test(61))  # Output: True
print(is_prime_test(4))  # Output: False
print(is_prime_test(1))  # Output: False
```
This Python function `is_prime` checks if a given number is prime, returning `True` if it is prime and `False` otherwise. The test function `is_prime_test` calls the `is_prime` function with various numbers and prints the results. This script is also contains self-contained code and passes all the test cases.