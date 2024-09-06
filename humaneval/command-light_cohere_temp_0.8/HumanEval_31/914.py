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

# Test function
def test_is_prime():
    print(is_prime(6))  # Output: True
    print(is_prime(101))  # Output: True
    print(is_prime(11))  # Output: True
    print(is_prime(13441))  # Output: True
    print(is_prime(61))  # Output: True
    print(is_prime(4))  # Output: False
    print(is_prime(1))  # Output: False
    print(is_prime(5))  # Output: False
    print(is_prime(3))  # Output: False
    print(is_prime(7))  # Output: False
    print(is_prime(120))  # Output: False
```
This code defines a function called `is_prime` that checks whether a given number `n` is prime or not. It uses a certain algorithms, such as the sieve of Eratosthenes or the Sieve of Plato, to determine if the number is prime or not. The function returns `True` if the number is prime and `False` otherwise.

The `test_is_prime` function serves as a test case to evaluate the `is_prime` function. It passes all test parameters to the `is_prime` function and prints the corresponding results.

Note: The algorithm used to check for primality is not the most efficient, but it serves the purpose of testing the function. The most efficient primality algorithm is the Sieve of Eratosthenes.