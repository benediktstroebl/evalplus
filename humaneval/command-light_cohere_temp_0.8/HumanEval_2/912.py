Here's a Python code that solves the problem of removing decimal portion of a number:
```python
def truncate_number(number: float) -> float:
    """
    Remove the decimal part of the number.
    """
    int_part = number // 1
    """

    return round(int_part)
```

This code uses integer division to remove the decimal part of a given number and then rounds it to return the integer portion.