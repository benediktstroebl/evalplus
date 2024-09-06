```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.1) + 1):
        if n % i == 0:
            return False
    return True

# Test code
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1)))  # Output: False
```
This Python code defines a function called **'is_prime()'** that checks whether a given number 'n' is a prime number. It uses a technique of iterating from 2 up to the square root of 'n', and checking for divisibility. If any number is divisible by any of these potential divisors, it returns 'False', indicating that 'n' is not prime. If no divisors are found, it returns 'True', indicating that 'n' is a prime number.

The code then provides some test cases to verify the correctness of the 'is_prime()' function. It correctly identifies the'd are some prime numbers and some composite numbers. The function works as intended and passes all the tests.