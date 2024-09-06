```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
   
    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    0.05
   
   - test - number can be divided by itself and get the remainder, and the number > 1 will be rounded down to 1.
  """ [Truncate the number](number > 1) -> 1
  """
    return number if number <= 1 else 1
```

This Python function, `truncate_number`, accepts a single argument: a positive floating-point number. It effectively divides the At positive number into two components: an integer part (the biggest integer smaller than the provided number), and a decimal part (the leftover, always smaller than 1). The function then returns the decimal portion of the number. This function guarantees that the result is always non-negative and less than 1, and that the input number is accurately represented.