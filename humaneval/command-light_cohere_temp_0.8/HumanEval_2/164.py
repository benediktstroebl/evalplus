```python
def truncate_number(number: float) -> float:
    """
    Returns the decimal part of a positive floating point number. 
    Args:
        number (float): positive floating point number

    Returns:
    float: decimal part of the number
    """
    assert number > 0
    return math.floor(number) + (number - math.floor(number)) * (1 / 10)
```
This code defines a function that takes a number as an argument and returns the decimal part of the number. 

This function uses an combination of math. Floor division and floor math to remove the fractional part of the number and returns the decimal part.