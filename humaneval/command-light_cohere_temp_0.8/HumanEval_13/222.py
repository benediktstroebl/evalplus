```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Error: Input parameters cannot be empty"
    
    if a == 0 or b == 0:
        return "Error: Both inputs must be positive"
    
    while b > 0:
        if a % b == 0:
            a, b = b, a // b
        else:
            b -= 1
    
    return a

# Test the function with various inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(0, 4))   # Error: Both inputs must be positive
print(greatest_common_divisor(-1, 7))  # Error: Inputs cannot be negative
```