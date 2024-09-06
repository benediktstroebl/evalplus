Here is a Python script that contains a self-contained function that solves the problem you have described. 
```python
def truncate_number(number: float) -> float:
    """
    >>> truncate_number(3.5) == 0.1
   0
   Truncate_number(3.5)
   0.1
```
This code defines a function called `truncate_number` that takes a single argument `number` which is a float value. It uses this value to create a new function, `decompose_number`, which returns the integer part of `number`. Then, it uses the `decompose_number` value to create a new function, `truncate_value`, which returns the decimal part of `number`.