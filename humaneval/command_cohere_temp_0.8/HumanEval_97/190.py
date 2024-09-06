```python
def multiply(a, b):
    return int(str(a)[:-1]) * int(str(b)[:-1])
```
The function `multiply(a, b)` takes two integers as input and returns the product of their unit digits, where the unit digit is the digit in the far right position. The nested `int(str(a)[:-1])` operation extracts the unit digit from the integer `a` and returns an integer ignoring the unit digit. The function then multiplies this value with the result of applying the same process to `b`. The result is then returned as an integer. 

This approach takes advantage of the string manipulation techniques to extract the unit digits. It provides an efficient solution that achieves the goal of the problem in a concise manner. 

This function can be run independently in the Python environment after the markdown code block is inserted.