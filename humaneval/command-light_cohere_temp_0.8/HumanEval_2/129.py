```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    number = number if number < 1 else number+1 
    return number // 1
    return f"{number}" if str(number).number.isdigit() else == "1" else  str(number)[0]
```