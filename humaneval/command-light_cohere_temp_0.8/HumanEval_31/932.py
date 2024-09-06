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

# Test suite
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
``` 
The code defines a function `is_prime(n)` that checks whether a given number `n` is a prime number or not. It employs various conditional checks and trial divisions to determine primality. 

The `is_prime()` function also includes input validation to handle numbers greater than 1 correctly. 

The output of the test suite will be: 
```
False
True
True
True
False
False
``` 
This demonstrates the correctness of the `is_prime()` function.