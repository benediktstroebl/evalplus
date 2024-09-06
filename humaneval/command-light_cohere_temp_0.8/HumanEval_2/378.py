```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Returns the decimal part of the number
    """
    return 0.1 if number <= 1 else number - decimal_part()

def decimal_part(number: float) -> float:
    """ Returns the decimal part of a number. 
    """
    decimal part is always less than 1. 
    """
    number = float(number) 
    while number > 1:
        number = number // 10 
    return number
```
The function decimal_part() computes the decimal part of a number, which is always less than 1. The function starts by converting the number to a float and then uses a while loop to repeatedly divide the number by 10 until the number becomes less than 1. This effectively extracts the fact that each iteration, the largest integer part smaller than the original number is removed, leaving only the decimal part.