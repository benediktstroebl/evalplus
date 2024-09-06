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

# Test case 1: Is 6 a prime?
print(is_prime(6))  # Output: False

# Test case 2: Is 101 a prime?
print(is_prime(101))  # Output: True

# Test case 3: Is 13441 a prime?
print(is_prime(13441))  # Output: True

# Test case 4: Is 61 a prime?
print(is_prime(61))  # Output: True

# Test case 5: Is 4 a prime?
print(is_prime(4))  # Output: False

# Test case 6: Is 1 a prime?
print(is_prime(1))  # Output: False
```

The function `is_prime(n)` determines whether a given number is a prime or not. It starts by examining if `n` is less than or equal to 1, in which case it is not prime, and returns `False`. It then examines if `n` is of the form 2 or 3, returning `True` if it is. If the number satisfies either condition, it returns `False`, indicating that `n` is not a prime number. 

The function then enters a loop that begins with `i = 5` and continues until the square of `i` is less than or equal to `n`. This loop checks for divisibility by testing if `n` is divisible by `i` or `i + 2`, and if it is, it returns `False`. If no divisibility is found, it returns `True`, indicating that `n` is a prime number. 

This function is self-contained and effectively determines whether a given number is prime or not, passing all the test cases.