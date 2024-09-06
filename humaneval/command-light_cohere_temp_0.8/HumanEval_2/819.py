Here's the corrected Python script with self-contained code to truncate a number to a specified precision:

```python
def truncate_number(number: float) -> float:
    """
    Return the decimal part of the number
    given a positive floating point number.
    """
    number = float(number)  # Convert string input to float

    # Convert to a string, ensuring maximum precision
    number_str = str(number)

    # Remove trailing zeros in decimal part
    number_str = number_str.split('.', 1)[0]

    # Return the truncated decimal part
    return float(number_str)
```

This script defines a function `truncate_number` that takes a float number as input and returns the decimal part of the number as a float value. The function first converts the number to a string using `str()` method, ensuring maximum precision. Then, it splits the decimal part of the string from the whole number string using the split method and selects the first element of the resulting tuple using indexing. Finally, it converts the string back to a float value to return the desired decimal part of the original number.