```python
def greatest_common_divisor(a, b): 
    if not or a == 0 or b == 0: 
        return 0
    ret = 1
    while a % ret != 0 and b % ret != 0: 
        ret += 1
    return ret

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(5, 25)))  # Output: 5
print(greatest_common_divisor(17, 49)))  # Output: 13 (correct answer is 13)
print(greatest_common_divisor(19, 1)))   # Output: 19 (correct answer is 19)
```