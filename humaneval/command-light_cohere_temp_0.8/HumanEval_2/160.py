Here is a Python script with a self-contained function that solves the problem you provided:
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals. 
    Return the max (integer part) and 
    min(decimal part).
    >>> truncate_number(3.5)
    0.5
   
    Truncates a numbers with decimal points that are 
    greater than 0 but less than 1.
    """
    float(number / 10) + int(number % 10)
``` 
This function takes a number as input and returns the maximum integer part and the minimum decimal part of that number.