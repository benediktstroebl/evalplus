```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equation from three different angles, and returns True if any of these equations are true, indicating a right triangle. 

Here are some examples of how this function can be called:
```python
>> right_angle_triangle(3, 4, 5)
True
>> right_angle_triangle(1, 2, 3)
False
```

This script will evaluate as intended for the given input examples provided in the original problem. 

This function is designed to be used with Python 3 and utilizes the `**` exponentiation operator, which is not available in earlier versions of Python. 

Please let me know if further clarification is needed!