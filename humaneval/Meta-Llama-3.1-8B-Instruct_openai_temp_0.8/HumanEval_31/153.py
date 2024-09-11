```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    :param n: The number to check for primality
    :type n: int
    :return: True if n is prime, False otherwise
    :rtype: bool
    """
    if n <= 1:  # Prime numbers are greater than 1
        return False
    elif n <= 3:  # 2 and 3 are prime numbers
        return True
    elif n % 2 == 0 or n % 3 == 0:  # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # Only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisibility by 6k ± 1
            return False
        i += 6
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime` that checks if a given number `n` is prime. It uses a basic algorithm to check for primality: it first handles the trivial cases where `n` is less than or equal to 1, or where `n` is 2 or 3; then it checks if `n` is divisible by 2 or 3; and finally, it checks for divisibility by 6k ± 1 up to the square root of `n`. The function returns True if `n` is prime, and False otherwise. The test cases are then executed to verify the correctness of the function.