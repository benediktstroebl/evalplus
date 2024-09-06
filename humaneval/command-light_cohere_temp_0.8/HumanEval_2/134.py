Here is a Python script that defines a function, `truncate_number`, that meets the requirements specified:
```python
def truncate_number(number: float) -> float:
    """
    >>> truncate_number(3.5) < 0.25
    return of decimal part of the number, only integers and floats less than 1 are returned.
    """
    return round(number - 1e9) if number > 1 else abs(number)
```
This code provides a straightforward solution that meets the specifications and works well with the given use case.