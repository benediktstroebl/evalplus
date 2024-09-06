Here's the corrected self-contained Python script with a function that truncates a positive floating-point number: 

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)  #.9529
    certain interesting decimal part of 3.5
   
    might be more meaningful and easy to understand without additional imports.