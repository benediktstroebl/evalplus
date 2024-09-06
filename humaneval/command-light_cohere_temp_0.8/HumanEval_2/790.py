```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    >>> truncate_number(3.5)
    NOTE: Will return 0.2
   
    number is not a decimal number. 

    < Return a number to 1e.0 and greater than decimal number.
    """  Note the  for floating point numbers, the decimal part is the fractional part after the decimal point.

    The function works by first taking the number as input, and then performing a sequence of mathematical operations. The first step involves rounding the number up to the largest integer that is less than the number. This is done by using the `round()` function, which rounds the number up to the nearest integer value. The result of the mathematical operation involves subtracting the largest integer that is less than the number from the number. The result of this operation is then assigned to the variable `int`, and the variable `decimal` is assigned the result of subtracting the largest integer from the number from the number.

Finally, the function returns the value of `decimal`, which is the decimal part of the number. This is mathematical approach is a simple and efficient way to obtain the decimal part of a floating point number.