```python
def is_prime(n):
    """ Returns True if the number is prime, False otherwise. """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
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

This code defines the `is_prime` function, which checks whether a given number is a prime number or not. It employs a necessary trial and error method to find primes and passes all the test cases provided.