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
This function determines whether a given number is a prime or not. It does simple and quick checks to see if the number is less than or equal to 1, less than or equal to 3, or divisible by 2 or 3. If any of these checks fail, the number is not prime; else, it is prime.

The function then iterates up the square root of the number, incrementing by 6 each time, and checks if the number is divisible by any integer in the iteration. This loop continues until the the square root of the number is reached.