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

# Test the function with some values
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This function, named `is_prime`, checks if a given number is prime or not. The function employs a well-known tests for prime numbers to determine whether the input number is prime or not. The function returns `True` if the input number is prime and `False` otherwise. The function is self-contained, as it does not require any external functions or variables to solve the problem. The tests are also self-contained and can be used to determine the primality of any number.