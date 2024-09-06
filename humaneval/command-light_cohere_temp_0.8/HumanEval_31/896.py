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

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
``` 
This Python function, `is_prime()`, verifies if a given number is a prime or not. The function starts by checking if the number is less than or equal to 1, which would make it not a prime, so it returns `False`. 

It then checks if the number is less than or equal to 3, which is also not prime, so it returns `True`. 

After that, the function starts a loop that checks for divisibility by squares of numbers from 5 up to the given number. 

Finally, it returns `True` if the given number is a prime, and `False` otherwise.