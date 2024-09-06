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
This code defines a function `is_prime` that checks whether a given number is a prime. It then passes the key tests using the function to check if different numbers are prime. It uses a simple and efficient algorithms to determine whether a number is prime or not, following the steps:
- If the number is less than or equal to 1, it is not prime.
- If the number is 2 or 3, it is prime.
- If the number is divisible by 2 or 3, it is not prime.
- If the number is a perfect square or can be expressed as the product of two primes, it is not prime.
- The number is a square number and is greater than 2, it is not prime.
- The number is of the form 5i + 2j, where i and j are integers, and both are less than the square root of the number.

The function returns `True` if the number is prime and `False` otherwise. The code then tests the function by passing different numbers to it and prints the result.