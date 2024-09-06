```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # get integer part
    integer = number // float('inf')
    # calculate the decimal part
    decimal = number - (integer * float('inf'))
    return decimal
```

This function takes a floating point number as input and returns the decimal part of that number. The function first calculates the region under the line of the number using floor division. Then, it subtracts the region multiplied by `inf`, which effectively gets rid of the integer part. This results in the decimal part of the number.