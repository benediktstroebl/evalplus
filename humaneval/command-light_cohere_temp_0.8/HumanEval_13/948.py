```python
def greatest_common_divisor(a, b): 
    if b == 0: 
        return a 
    elif a == 0: 
        return b 
    else: 
        return greatest_common_divisor(b, a % b) 

# Tests
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(10, 15)))  # Should print None, as 10 is not divisible by any number
print(greatest_common_divisor(7, 8)))  # Should print None, as 7 is not divisible by any number
```