```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Incorrect input values: a or b is empty")
    
    if a == 0 or b == 0:
        return 0
    
    # Determine the greater number
    if a > b:
        a, b = b, a
    
    # Calculate the common divisor using the formula
    result = a // b
    if result == 0:
        raise ValueError("Cannot divide by zero")
    
    return result

# Unit tests
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(-5))  # Output: ValueError: Incorrect input values: a or b is empty
print(greatest_common_divisor(10, 20))  # Output: ValueError: Cannot divide by zero
```