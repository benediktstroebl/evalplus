```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # Assuming positive number
    int_part = int(number)
    decimals = number - int_part
    return decimals
```
Do you need anything else to help me with?