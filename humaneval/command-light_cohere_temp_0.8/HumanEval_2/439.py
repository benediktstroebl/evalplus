```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    #Integer part of the number
    int_part = number // float('inf')

    """
    Decimals part of the number (exclusive of 1)
    decimals = [float(num) for num in str(number).replace('.', '').replace('.', '').replace('', '', '').format(int_part)]
    return int_part + decimals[-1]
```