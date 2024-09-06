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
This Python code defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. The function employs several heuristic primality tests, such as dividing by 2 and 3, checking divisibility by consecutive odd numbers, and checking for factors of the form of squares and multiples of 6.

The output of this code will be: 
```bash
False
True
True
True
False
False
``` 
This is consistent with the behavior of the is_prime function. 
Note: This function is not a exhaustive primality test and does not guarantee to catch all prime numbers, but it provides a simple and efficient approach for most practical purposes.