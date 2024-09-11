```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
```

This script defines a function called `truncate_number` that takes a floating point number as an argument. The function works by subtracting the integer part of the number (obtained by converting the number to an integer with `int(number)`) from the original number, effectively isolating the decimal part.

The script also includes a docstring that explains how to use the function and what it returns, as well as an example usage of the function.