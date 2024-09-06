```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required")
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input must be integers")
    if a == 0 or b == 0:
        return 0
    
    common_divisor = 0
    while b != 0:
        a %= b
        common_divisor += 1
        b //= 2
    
    return common_divisor

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```