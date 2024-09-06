```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0:
        a, b = divmod(a, b)
    
    return b

# Example usage
a = 25
b = 15
print(greatest_common_divisor(a, b))  # Output: 5
```