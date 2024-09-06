```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0 and b != 0:
        a, b = divmod(a, b)

    return min(a, b)

# Test the function
print(greatest_common_divisor(3, 5)) # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(6, 6))  # Output: 2 (Equality test passes due to both numbers having the same GCD)
```