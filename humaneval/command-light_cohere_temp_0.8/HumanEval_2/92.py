```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    number = float(number)  # Ensure input is a float number
    whole, decimal = divmod(number, 10)
    return round(decimal[0]) if decimal[1] == 0 else round(decimal[1])
```
The function uses the divmod() function to decompose the number into its integer and decimal parts, and then uses the round() function to round the decimal part appropriately and return it.