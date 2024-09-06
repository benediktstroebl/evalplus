```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    # Convert number to fraction
    number_as_fraction = number / 10**(min(10, 5 - (number.id - 1))
    
    # Return integer part
    integer_part = 10**min(10, 5 - number.id - 1) * 10**(number_as_fraction - 1)
    
    return (number_as_fraction * integer_part)
```