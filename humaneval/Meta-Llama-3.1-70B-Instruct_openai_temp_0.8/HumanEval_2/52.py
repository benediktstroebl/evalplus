```python
def truncate_number(number: float) -> float:
    """
    Returns the decimal part of a given positive floating point number.

    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Raises:
    ValueError: If the input number is not a positive floating point number.
    """
    if not isinstance(number, float) or number < 0:
        raise ValueError("Input must be a positive floating point number.")

    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part


# Example use case
print(truncate_number(3.5))  # Output: 0.5
```
This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. It first checks if the input is a positive floating point number and raises a `ValueError` if it's not. Then, it calculates the integer part of the number by converting it to an integer, and subtracts this integer part from the original number to get the decimal part. Finally, it returns the decimal part.

You can use this function by calling it with a positive floating point number as argument, like in the example use case shown at the end of the script.