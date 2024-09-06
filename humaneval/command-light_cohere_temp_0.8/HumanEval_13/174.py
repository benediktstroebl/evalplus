```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    max_num = 1
    for i in range(1, min(len(a), len(b)) + 1):
        if a % i == 0 and b % i == 0:
            max_num = max(max_num, i)
    
    return max_num

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(56, 112))  # Output: 4
print(greatest_common_divisor(72, 24))  # Output: 2
```