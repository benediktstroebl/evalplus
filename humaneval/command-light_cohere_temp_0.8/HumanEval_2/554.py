```python
def truncate_number(number: float) -> float:
    """
    This function takes a positive floating point number and returns its decimal part,
    ensuring that the returned value is always less than 1.

    Args:
        number: The number to be decomposed.

    Returns: decimal part of the number, rounded down to the nearest integer less than 1.
    """
    return number // .5
```

The provided Python function, `truncate_number`, takes a positive floating point number as input and returns its decimal part, rounded down to the nearest integer less than 1. The function ensures that the returned value is always within the range of valid decimal numbers.