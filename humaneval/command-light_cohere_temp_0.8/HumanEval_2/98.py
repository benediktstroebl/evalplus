```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.05
   
    Region 1:
    - Positive numbers
    - Input: 3.5
    - Output: 0.05

    - Test case: True

    Region 2:
    - Floating point numbers
    - Input: 0.000
    - Output: 0

    Region 3:
    - Negative numbers
    - Input: -3.5
    - Output: 0

    Region 4:
    - Numbers smaller than 1
    - Input: 1.01
    - Output: 0

    Region 5:
    - Input: complex number
    - Input: 5.0
    - Output: 5.00

    - Test case: False
```