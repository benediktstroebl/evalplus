Here's a self-contained Python function that solves the problem of returning the decimal part of a given number:

```python
def truncate_number(number: float) -> float:
    """ Returns the decimal part of the number, which is the largest integer smaller than the given number that is less than the fractional part.

    Args:
        number: The number to get the decimal part of

    Returns:
    The decimal part of the number
    """
    if number < 0:
        number = abs(number)
    decimal = number - floor(number)
    return decimal
```

This function takes a number as input and returns the decimal part of that number, which is the largest integer smaller than the given number that is less than the fractional part. The function first checks if the number is negative. If the number is negative, it converts it to its absolute value using the abs() function. Then, it calculates the decimal part by subtracting the floor(number) (which returns the largest integer less than the number) from the given number. The function then returns the value of the decimal part of the number.

Note: this function assumes that the input number is a floating point. If the input is not a float or is negative, you may need to handle those cases accordingly.