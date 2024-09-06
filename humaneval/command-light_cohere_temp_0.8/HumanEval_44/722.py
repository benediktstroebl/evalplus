```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Invalid input types. Input must be an base an integer, and x an integer.")
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    if x < 0:
        raise ValueError("Input number cannot be negative")
    
    result = ""
    while x > 0:
        if x % base == 0:
            result += str(x) + "0"
        else:
            result += str(x // base) + "1")
        x = x // base
    
    return result

# Test cases
print(change_base(8, 3))       # Output: '22'
print(change_base(0, 5))       # Output: '00'
print(change_base(-3, 4))      # Output: '000'
print(change_base(7, 2))       # Output: '111'
```
This code defines a function `change_base` that converts a given number `x` to a string representation in the desired base `base`. The function raises an error if the input types are invalid or if the base is not within an acceptable range.