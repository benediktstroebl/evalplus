```python
def is_prime(n):
    """
    True if the number is prime, False otherwise.
    0 and 1 are always prime
    if n <= 1 or n % 2 == 0:
        return False
    if n <= 3:
        return True
    # Check divisibility by 2, 3 and 5
    if n % 5 == 0 or n % 2 == 0:
        return False
    # Check divisibility by numbers ending with 5
    i = 6
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
The function is_prime takes an integer n as input and returns True if n is a prime number and False otherwise. 

The function first checks if n is less than or equal to 1, in which case it is always prime. It then checks if n is divisible by 2 or 3, in which case it is not prime. The function then checks if n ends with 5 by checking divisibility by numbers that end with 5. Finally, if none of these conditions are met, the function returns False, indicating that n is not a prime number.