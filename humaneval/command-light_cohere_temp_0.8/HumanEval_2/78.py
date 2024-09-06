```python
def truncate_number(n: float) -> float:
    """
    Return the decimal part of the number, given a positive floating point number.
    """
    decompose theformed as a tuple, (int, float)
    """
    if n < 0:
        raise ValueError("Input must be a positive number.")
    int_part, dec_part = divmod(n, 10)
    return dec_part
```
This script defines a function `truncate_number` that returns the decimal part of a positive floating point number `n`. The function is designed to handle negative numbers and return an error for them. 

The function uses the `divmod` function to split the number into an integer and a decimal part, and then returns the decimal part of the number.