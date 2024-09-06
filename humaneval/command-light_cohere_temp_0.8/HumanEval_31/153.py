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
This code defines a function called is_prime that takes an integer n as input and returns true if n is a prime number and false otherwise. It uses a specific conditions and trial and error methods to check for prime numbers, following the idea of trial divisions by squares and other small primes. The function also passes all the specific tests, which are the same as the ones in the original problem.