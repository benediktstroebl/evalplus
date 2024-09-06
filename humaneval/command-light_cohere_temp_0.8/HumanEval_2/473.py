```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return the decimal part of the number
    """
    number = float(number)
    int_part = int(number)
    dec_part = str(number)[-2:] 
    return float(int_part) + float(dec_part)
``` 
Test the function with a few cases.