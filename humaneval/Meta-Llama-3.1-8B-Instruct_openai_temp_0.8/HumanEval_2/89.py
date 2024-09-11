```python
def truncate_number(number: float) -> float:
    """
    This function decomposes a positive floating point number into its integer part 
    and decimal part. The integer part is the largest integer smaller than the given number.
    The function returns the decimal part.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    return number - int(number)  # Subtract the integer part from the number to get the decimal part


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(12.75))  # Output: 0.75
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The function works by subtracting the integer part of the number from the number itself, effectively leaving only the decimal part. The example usage demonstrates how to use this function with different inputs.