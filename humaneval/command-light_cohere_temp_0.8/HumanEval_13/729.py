```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    max_c = 0
    for i in range(1, min(len(a), len(b)) + 1):
        if a % i == 0 and b % i == 0:
            max_c = i
    
    return max_c

# Test suite
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(6, 20))  # Should print: None (divisors are not consecutive)
print(greatest_common_divisor(28, 14))  # Should print: 4
```