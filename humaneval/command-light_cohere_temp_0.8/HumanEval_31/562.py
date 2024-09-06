Here is a Python script with a self-contained function that solves the problem and passes the tests you provided:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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

# Test case 1
print(is_prime(6))  # Output: False

# Test case 2
print(is_prime(101))  # Output: True

# Test case 3
print(is_prime(11))  # Output: True

# Test case 4
print(is_prime(13441))  # Output: True

# Test case 5
print(is_prime(61))  # Output: True

# Test case 6
print(is_prime(4))  # Output: False

# Test case 7
print(is_prime(1))  # Output: False)
```
This Python code defines a function named `is_prime` that checks whether a given number is prime or not. It employs various conditions and divisibility checks to determine whether a number is prime or not. The function returns `True` if the input is a prime number and `False` otherwise. It also includes several test cases to validate the correctness of the `is_prime` function. 
The output of each test case will display the result of calling the `is_prime` function with the corresponding input.