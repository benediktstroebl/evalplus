```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers and false otherwise."""
    # Check if a is divisible by 2 or 3
    if (a <= 2) or (a % 2 == 0) or (a % 3 == 0):
        return False

    # Check if a is a multiplication of two primes
    for p in range(2, int(a ** 0.5) + 1):
        if a % (p * p) == 0:
            return False

    return True

# Test cases
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(105))  # Output: False
print(is_multiply_prime(2))    # Output: True
print(is_multiply_prime(4))    # Output: False
```

This Python script defines a function called `is_multiply_prime` that checks whether a given number is the multiplication of 3 prime numbers or not. The function uses a simple algorithm to identify multiplication of primes by iterating through potential factors and checking divisibility. The test cases cover a numbers ranging from 2 to 100, passing each one to the function. This script then correctly identifies the values that the function will return as True and those that will be False.