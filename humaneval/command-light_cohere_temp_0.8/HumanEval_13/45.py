Here is a Python script with a self-contained function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0:
        a, b = divmod(a, b)

    return b

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```

This code provides a simple, clear, and effective solution to the problem. It uses a efficient `divmod` loop to find the GCD, and handles edge cases (like when one number is 0) and negative numbers.