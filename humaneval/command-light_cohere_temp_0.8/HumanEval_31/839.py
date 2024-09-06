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

The function 'is_prime' takes an integer 'n' as input and returns 'True' if 'n' is a prime number and 'False' otherwise. Prime composition of the at the specific methods to check if a number is prime, and then uses a loop to iterate up to the square root of 'n', checking for divisibility.  The number. specific numbers, such numbers up a function for prime numbers and is relatively efficient for small inputs.