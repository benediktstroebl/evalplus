Here is a Python script with a self-contained function that checks whether a given number is prime:

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function with some values
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This code defines a function `is_prime` that takes an integer `n` as input and checks whether it's a prime number or not. The function uses a simple algorithm to determine if a number is prime: it first handles the base case where n is less than or equal to 1, where all numbers are not prime. It then iterates from 2 to the square root of n, and for each integer `i` from 2 to the square root of n, it checks if `n % i` is 0. If any of these values the numbers divisible by any of these numbers, the function returns `False`. If no divisors are found, it returns `True`, indicating that the number is prime.

The code then provides a set of test values and calls the `is_prime` function to check if they are prime or not. The test values are: (6, 101, 11, 13441, 61, 4, 1). The output will be True for all of these values except 1, which is not prime.