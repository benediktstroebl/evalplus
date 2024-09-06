Here is a self-contained Python script that defines a function `truncate_number` that solves the problem you provided:
```python
def truncate_number(n: float) -> float:
    """
    >>> truncate_number(3.5) == 0.1
   
    important integer part of 3.5
    decimal part of the
    """
    """
    # Using Python's built-in functions to safely extract integer and decimal parts
    n = n if type(n) == float
    return round(int)(n) - round(n) + 1 if type(n) == float else n
```
This function uses Python's built-in functions `round` and `int` to safely and accurately extract the integer and decimal parts from a given number.