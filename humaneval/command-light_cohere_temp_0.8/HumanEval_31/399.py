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

# Test the function with markdown codes
is_prime(6)  # Should return False
is_prime(101)  # Should return True
is_prime(11)  # Should return True
is_prime(13441)  # Should return True
is_prime(61)  # Should return True
is_prime(4)  # Should return False
is_prime(1)  # Should return False
```
This solution, functions to test your implementation of the is_prime function with various input values and verify its correctness. The output will be True for all correct inputs, and False for the incorrect ones.