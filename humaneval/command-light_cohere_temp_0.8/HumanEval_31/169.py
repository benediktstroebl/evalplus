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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This code defines the function is_prime(n) that checks whether a given number is prime or not. It uses the simple algorithm to determine primality: If the number is less than or equal to 1, it's not prime; otherwise, it checks for divisibility by 2 and 3, and then, it uses a simple loop to check for divisibility by prime numbers up to the square root of the number, ensuring that the loop terminates when the number is greater than the square root of the number. The code then passes all test cases for the function and can be used as a reference to test the function's correctness.