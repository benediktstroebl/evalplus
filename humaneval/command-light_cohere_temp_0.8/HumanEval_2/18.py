```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number

    Test cases:
    >>> truncate_number(3.5)
   
    0.5
   
    expected output: 0.25
    Test cases:
    - even numbers
    - floats
    - strings
    - complex numbers

    """
    number = float(number)
    if number <= 1:
        return 0.0
    elif number < 2:
        return 0.5
    else:
        return number - 2
```