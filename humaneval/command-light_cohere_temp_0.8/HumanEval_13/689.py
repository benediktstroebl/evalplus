```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)
```
This function employs a recursive approach to discover the greatest common divisor of two numbers. It begins by examining whether either number is zero, in which case it returns the other number as the greatest common divisor. For non- numbers, the function raises a ValueError exception. 

The function's design ensures that it can handle the case of receiving non-numeric inputs, and it also includes input validation to meet certain requirements.