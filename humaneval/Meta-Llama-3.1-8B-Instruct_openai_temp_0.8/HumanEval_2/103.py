```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it returns the decimal part.

    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Example usage
print(truncate_number(3.5))  # 0.5
print(truncate_number(10.7))  # 0.7
print(truncate_number(2.0))  # 0.0
```

This Python script defines a function `truncate_number` that takes a positive floating point number and returns its decimal part. The decimal part is obtained by subtracting the integer part of the number from the number itself. The function includes a docstring that provides a description, lists the function's arguments and return values, and includes doctest examples.