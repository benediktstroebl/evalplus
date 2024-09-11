```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    :param n: The number to check for primality
    :return: True if the number is prime, False otherwise
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Only need to check up to the square root of n
        if n % i == 0:  # If n is divisible by any number in this range, it's not prime
            return False
    return True  # If n is not divisible by any number in the range, it's prime

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It uses a simple trial division method to check for primality. The function iterates over all numbers up to the square root of `n` and checks if `n` is divisible by any of them. If `n` is divisible by any number in this range, it's not prime. If it's not divisible by any number in the range, it's prime. The function returns `False` for numbers less than or equal to 1, as they are not prime.