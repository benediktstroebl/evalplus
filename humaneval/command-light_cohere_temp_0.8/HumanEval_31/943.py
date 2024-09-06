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

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This Python function, 'is_prime(n)', determines whether a given number is prime or not. It quickly checks the basic conditions for prime numbers and employs a loop to confirm primality beyond the square root of the number. The function's test cases pass successfully and demonstrate the use of the function.

The function uses the condition 'n <= 1', which is always false for prime numbers, to quickly identify non-prime numbers. It then applies a basic primality tests: checking if 'n' is less than or equal to 2 or 3, or checking if 'n' is divisible by 2 or 3. If any of these conditions are met, the function returns 'False', indicating that 'n' is not a prime number. If none of these conditions are met, the function returns 'True', indicating that 'n' is a prime number.