```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # ensure positive number
    number = number if number < 0 else number + 1
    
    # integer part
    i = int(number)
    
    # decimal part
    d = number - i
    
    return d
```