```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # split number into integer and decimal part
    i, d = divmod(n, 1)
    return d
```
This code defines a function called `truncate_number` that takes a single argument `n` which is a float value. The function returns the`n decimal part of the number. 

The function uses the `divmod` function to split the given number into an integer part and a decimal part. The function then returns the decimal part of the number.