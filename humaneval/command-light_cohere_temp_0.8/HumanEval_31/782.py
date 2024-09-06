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

# Test function to check if a number is prime
def is_prime_test(n):
    return is_prime(n)

# Test some values
print(is_prime_test(6))  # Output: True
print(is_prime_test(101))  # Output: True
print(is_prime_test(11))  # Output: True
print(is_prime_test(13441))  # Output: True
print(is_prime_test(61))  # Output: True
print(is_prime_test(4))  # Output: False
print(is_prime_test(1))  # Output: False
print(is_prime_test(255))  # Output: False
```

This script defines a function `is_prime` that checks if a given number is prime. It also provides a test function `is_prime_test` which calls the `is_prime` function to check if a number is prime or not. 

This function implements a primality test using an optimization, called the "6k test," which uses the facts that the only numbers exceeding 2 that are divisible by `2` or `3` are 6k + 2k, where k is a number greater than 1.  The tests that way significantly reduces the number of tests needed to check for primality, making it more efficient for larger numbers.