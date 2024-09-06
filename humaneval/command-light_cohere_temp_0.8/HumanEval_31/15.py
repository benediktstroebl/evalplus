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

This Python function, `is_prime()`, determines whether a given number is a prime or not. The function employs trial and error by testing divisibility from 2 to the square root of the number, along with testing numbers that are congruitant to the square root. 

This method can be quite efficient for large numbers as it doesn't involve looping for all numbers less than or equal to the square root of `n`.  The function returns `True` if the given number is prime and `False` otherwise.  The also checks the specific cases where 2 and 3 are not prime, and also, it avoids the common trap of testing only up to the square root of `n`.