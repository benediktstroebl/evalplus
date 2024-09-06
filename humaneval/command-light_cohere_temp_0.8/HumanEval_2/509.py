```python
def truncate_number(number: float) -> float:
    """
    Return the decimal part of the number.
    """
    integer_part = int(number)
    decimals = number - integer_part
    return decimals
    ```

This function takes a number as an argument and returns the decimal part of that number. It achieves this by first extracting the integer part from the number, then calculating the difference between the number and the integer part. The difference is then subtracted from the number to get the decimal part. The function then returns the decimal part of the number.