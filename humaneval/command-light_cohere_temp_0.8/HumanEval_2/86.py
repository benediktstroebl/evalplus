```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    integer = bin(number).split('.')[0]
    decimal = bin(number)[2:]
    return float(int(decimal[0:int(decimal)//10)])
``` 

This function takes a number as input, and returns the decimal part of the number. The function uses the other techniques, such as using the bin() function to extract the integer and decimal parts of a floating point number, and then converting the decimal part to a float value to get the desired result.