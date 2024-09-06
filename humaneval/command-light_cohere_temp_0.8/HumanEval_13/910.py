```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers must be provided")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Input must be integers")
    
    if a == 0 or b == 0:
        return 0
    
    common_divisor = 1
    while a != 0:
        while b % common_divisor == 0:
            common_divisor += 1
        b //= common_divisor
        
    return common_divisor

# Example usage 
>>> greatest_common_divisor(3, 5) # Output: 1
>>> greatest_common_divisor(25, 15) # Output: 5
```