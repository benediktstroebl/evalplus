```python
def truncate_number(n: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number

    Test cases:
    - Test with negative numbers
    >>> truncate_number(-3.5) == 0.0
   f also work with decimals
    - Test with floating point numbers
    >>> truncate_number(3.2) == 0.05

   
    dry
  test (no leftover):
    >>> truncate_number(0.00) == 0
   0
    - Test with decimals
    >>> truncate_number(1.360) == 1
   0.0001
```