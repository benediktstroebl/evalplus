```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Error: Input numbers a and b are empty"
    
    if a == 0 or b == 0:
        return "Error: Both input numbers are zero"
    
    m, n = divmod(a, b)
    if m == 0 or n == 0:
        return "Error: Both numbers have a common divisor"
    
    return m + n

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```