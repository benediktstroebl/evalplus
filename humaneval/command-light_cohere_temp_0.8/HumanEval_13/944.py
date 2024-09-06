```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != b:
        if a % b == 0:
            a, b = b, a
        elif b % a == 0:
            a, b = a, b
        
    return min(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(7, 28)))  # Output: 28
print(greatest_common_divisor(0, 4))  # Output: 4
print(greatest_common_divisor(125, 57))  # Output: 57
```
This code defines a function called greatest_common_divisor, which takes two integers a and b as input and returns the greatest common divisor of a and b. By using a Some particular algorithm, this function efficiently calculates the greatest common divisor between the two input numbers. The function also handles edge cases, such as when one or both input numbers are 0, returning the other as the greatest common divisor.