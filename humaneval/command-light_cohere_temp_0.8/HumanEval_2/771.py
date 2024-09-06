Here's a self-contained Python function that reverts an input number into a truncated decimal representation:

```python
def truncate_number(number: float) -> float:
    """
    Args:
        number: positive floating point number

    Returns:
        float: decimal part of the number, rounded to the nearest integer smaller than the number.
    """
    number = float(number)
    result = int(number - (number >= 1))
    return result
```

This function takes a positive floating point number as an argument and returns the decimal part of the number, rounded to the nearest integer smaller than the number.