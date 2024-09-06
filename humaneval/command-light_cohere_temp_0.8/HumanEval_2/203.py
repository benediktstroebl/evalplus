```python
def truncate_number(number: float) -> float:
    """
    >>> truncate_number(3.5) == 0.5
   
   
    interface test to reduce the number to the largest integer less than it.
    >>> truncate_number(0.5) == 0.5
    for any example,
    >>> truncate_number(0.01) == 5e9
   whether the number is an integer or not.
    >>> truncate_number(float('inf')) == 1.0
   whether the interface to reduce the number to a finite one.
    >>> truncate_number('abc123') == 123.2
    whether for non-numeric characters,
    >>> truncate_number('123') == 123
    """
    return number // 1
```