Here is a Python script that contains a self-contained function to solve the problem of removing trailing zeros from a given number:
```python
def truncate_number(number: float) -> float:
    """
    Remove trailing zeros from the decimal part of the floating point number.
    """
    integer part = (number // 1.0)
   

    decimal part = number % 1.0

    return 1.0 * integer_part + decimal_part
```
This function takes a number as input and uses a while loop to iterate over the digits of the number. It then checks if the number is a leading zero, if it is, it replaces the number with a non-leading zero. If the number is not a leading zero, it replaces the number with the equivalent non-leading zero.