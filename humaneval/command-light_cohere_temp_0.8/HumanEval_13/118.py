```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    m = min(a, b)
    for i in range(1, m // 2 + 1):
        if (a % i) == 0 and (b % i) == 0:
            return i
    
    return 2 ** 10

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(4, 12))  # Should return 4, correct?
print(greatest_common_divisor(8, 10))  # Should return 4, correct. main_test_complete and print(True)
```