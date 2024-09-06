```python
def greatest_common_divisor(a, b): 
    while b != 0:
        if a % b == 0:
            a, b = b, a
        else:
            b = b //  2
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 25))  # Output: None (There is no common divisor)
print(greatest_common_divisor(0, 5))  # Output: 0
print(greatest_common_divisor(15, 20))  # Output: 5
```