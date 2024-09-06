Here's the code:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: The decimal part of the number.
    """
    number = float(number)
    decimal = abs(number) - int(abs(number))
    return decimal
```