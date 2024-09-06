```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    < 0.5
   
    smaller than a decimal part of the number 3.5 in base 10.0.
    """
    value of decimal part of a number

    """
    number = number  # convert the input to a float.
    integer = int(number)  # get the largest integer smaller than number
    decimal = round(number - integer)  # get the decimal part
    return decimal
``` 
This Python code defines a function called `truncate_number` that takes a single argument, a float number, and returns the decimal part of that number. The decimal part is obtained by subtracting the largest integer less than the number from the number and then rounding the result to get the smallest integer.