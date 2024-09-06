Here's the Python code that solves the problem you described: 

```python
def truncate_number(number: float) -> float:
    """
    >>> truncate_number(3.5) == 0.25
   
    number can bigger floating point number, it can be decomposed into an integer part and a decimal part (the decimal part is always less than 1).
    Return the decimal part of the number
    """
    if number < 0:
        raise ValueError("Input number must be a positive float")
    elif number <= 1:
        return 0.0
    elif abs(number) <= 3:
        return number - 1.0
    else:
        return float("Output not supported")
```

This script provides a function `truncate_number` that receives a positive floating point number and returns the decimal part of the number. The output is always a finite number, either 0 or a positive integer less than 1. The function also raises a ValueError if the input number is negative or greater than 3.