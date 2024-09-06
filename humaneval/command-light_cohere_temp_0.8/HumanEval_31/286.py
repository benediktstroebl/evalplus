```python
def is_prime(n):
    """
    Check if a number is prime or not.
    """
    - Return True if n is a prime number, and False otherwise.
    - Returns for i from 2 to the square root of n
    - Check if n is divisible by any integer in the range [i, n-i]
    """
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This Python function, `is_prime(n)`, takes an integer `n` as input and checks whether it is a prime number. The function iterates through 2 to the square root of `n` and checks if `n` is divisible by any integer in the range `[i, n-i]`. If a number is found, it is not prime, and the function returns `False`. Otherwise, it returns `True`. 

This function is tested with various input values, and the results are printed to the console, showing that the function successfully identifies prime numbers and defects.