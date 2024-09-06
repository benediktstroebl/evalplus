Here is a self-contained Python function that solves the problem of removing trailing decimals from a positive floating point number:
```python
def truncate_number(number: float) -> float:
    """
    Remove trailing decimals from a positive floating point number.
    Remove trailing zeros and numbers ending with . float and integer part are returned.
    """
    number = str(number)
    integer_part = int(number[::-1])
    return float(number.replace('.' stretches for ' of ' if ' is not a decimal, otherwise, 
    it searches for the next '.)

The function will return the integer part of the number, which will be the largest integer smaller than the original number.