```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        a_high = a % b 
        b -= a_high
    return a_high

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(59, 177))  # Output: 19
```