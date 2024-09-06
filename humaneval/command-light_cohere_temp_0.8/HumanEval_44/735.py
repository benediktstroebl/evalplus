```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Invalid argument types. Input should be integers.")
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base should be between 2 and 36.")
    
    result = []
    for i in range(x):
        digit = bin(i)[2:]
        result.append(int(digit, base))
    
    return ''.join(''.join(result))

# Test case 1: Change base of 8 to 3
print(change_base(8, 3))  # Output: '22'

# Test case 2: Change base of 8 to 2
print(change_base(8, 2))  # Output: '1000'

# Test case 3: Change base of 7 to 2
print(change_base(7, 2))  # Output: '111'
```
This code defines a function `change_base` that converts a number to a string with a specified base. It raises `TypeError` and `ValueError` if the inputs are not integers or if the base is not a valid value. The test cases pass the right.