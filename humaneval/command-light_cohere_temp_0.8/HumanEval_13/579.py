```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        if a % b == 0: 
            a ^= b
        b = b // a 
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(58, 45))  # Output: 29
print(greatest_common_divisor(0, 4))    # Output: 0
print(greatest_common_divisor(17, 49))  # Output: 1 (only 17)
```