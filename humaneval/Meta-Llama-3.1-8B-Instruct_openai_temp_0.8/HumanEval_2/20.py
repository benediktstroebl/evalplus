### Truncating Decimal Part of a Number
#### Problem Statement

Given a positive floating point number, decompose it into its integer part and decimal part, and return the decimal part.

#### Solution
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, return its decimal part.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the input number.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # Use the % operator to get the remainder of the division of the number by 1
    # This will give us the decimal part of the number
    decimal_part = number % 1
    
    # Return the decimal part, but ensure it's not zero (i.e., the number is an integer)
    # If the number is an integer, any number of decimal places will be zero
    return decimal_part if decimal_part!= 0 else 0.0
```
You can use this function to get the decimal part of any positive floating point number. Note that if the input number is an integer, the function will return 0.0, as it has no decimal part.