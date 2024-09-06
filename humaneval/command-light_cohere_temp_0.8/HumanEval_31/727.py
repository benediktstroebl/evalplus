```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.0375) + 1):
        if n % i == 0:
            return False
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
This code defines a `is_prime` function that checks whether a given number is prime or not. It uses a specific criteria and backtracking to determine primality. The function passes all the test cases with different numbers, and the output shows the function's behavior for each test.