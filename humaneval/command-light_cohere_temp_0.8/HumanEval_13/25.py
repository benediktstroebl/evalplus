```python
def greatest_common_divisor(a, b): 
    if b == 0: return a
    elif a == 0: return b
    else: 
        return greatest_common_divisor(b, a % b) 
    return b

# Example function call
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(5, 125)))  # Output: 5
print(greatest_common_divisor(111, 7))  # Output: 7 (since 111=11*7)
```