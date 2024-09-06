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
This code defines a `is_prime` function that checks if a given number is prime. The function employs a well-known sieve of Eratosthenes algorithm. It first handles small values of `n` and returns `True` if the number is prime, and `False` otherwise. The function then checks divisibility by 2 and 3, and then iterates through square numbers, testing for divisibility by their square root and `(i + 2)`. The function eventually returns `True` if no divisors are found within the given range.