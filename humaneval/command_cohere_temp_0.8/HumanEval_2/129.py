```python
def truncate_number(number):
    """ Returns the decimal part of the number
    Args:
        number (float): positive floating point number
    Returns:
        float: decimal part of the number
    """
    return number - int(number)
```

To better understand the logic behind the code, here is an explanation of how the `truncate_number` function works:
The function takes a single argument, number, which is a positive floating-point number. It returns the decimal part of the number as a float.

The decimal part is calculated by finding the difference between the original number and the closest integer less than or equal to the original number. This can be achieved using the int() function, which returns the closest integer value when applied to a float. Subtracting this integer from the original number yields the decimal part.

For example, let's take the input number `3.5`. When we apply the `int()` function to it, we get `3`, the closest integer less than or equal to `3.5`. Subtracting `3` from `3.5` gives us `0.5`, which is the decimal part of `3.5`.

The function returns this decimal part, allowing you to capture and work with just the fractional part of the original number.