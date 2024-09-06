```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # Assuming number is positive, it can be decomposed into integer and decimal part
    integer = int(number)
    decimal = number - integer
    return decimal
```

This function takes a floating point number as an argument and returns the decimal part of the number. It does this following:
- It assumes that the given number is positive.
- It uses the built-in function int() to extract the integer part of the number.
- It then subtracts the integer part from the original number to get the decimal part.

The function is self-contained, and it does not require any external functions or variables. It can be easily tested and used directly within a Python script.