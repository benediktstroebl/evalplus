```python
def is_prime(n):
    """Returns true if the number is prime, else false."""
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

# Test the function with a few examples
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
``` 
This function, `is_prime()`, takes an integer `n` as an argument and returns `True` if `n` is a prime number and `False` otherwise. The function uses basic criteria for prime numbers, such as numbers less than 2 and 3, and numbers that are divisors of other prime numbers, to determine if `n` is prime. 

This self-contained Python function is designed to efficiently determine whether a given number is a prime number or not, and it passes all the provided tests with the provided examples without any external dependencies.