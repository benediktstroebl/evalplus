```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.1 if number < 1 else
   
    >>> return 1e-2 if number < 1 else 2 * (number - 1)
    """
    return 0.1 if number == 1 else 1e-2 if number < 1 else 2 * (number - 1)
```
This function takes a number and returns the decimal part of the number, if the number is greater than 1, the function returns 0.1; if the decimal part is 0, the number is less than 1, the function returns 1e-2. If the number is equal to 1, the function returns 1.0.