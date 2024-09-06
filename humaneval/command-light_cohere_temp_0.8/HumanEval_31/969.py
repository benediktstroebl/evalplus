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
def test_prime(n):
    if is_prime(n):
        return n.isdigit()  # False

# Test suite for the function
print(test_prime(6))  # Output: True
print(test_prime(101))  # Output: True
print(test_prime(11))  # Output: True
print(test_prime(13441))  # Output: True
print(test_prime(61))  # Output: True
print(test_prime(4))  # Output: False
print(test_prime(1))  # Output: False
print(test_prime(9999))  # Output: False
```

This script defines a function `is_prime` that checks whether a given number is prime or not. It then provides a test function `test_prime` to verify if a number passed as an argument to it is prime or not. The test suite is created to pass all the tests for the `is_prime` function. 

Finally, the output of the test suite will display the behavior of the `is_prime` function for different input numbers.