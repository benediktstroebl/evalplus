```python
def truncate_number(number: float) -> float:
    """ Return the decimal part of a positive floating point number.

    Args:
        number (float): A positive floating point number to truncate.

    Returns:
        float: The decimal part of the input.
    """
    return number - // int(number)
```