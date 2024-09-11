```markdown
## Truncating the Decimal Part of a Floating Point Number

### Problem Definition

Given a positive floating point number, decompose it into its integer and decimal parts.
Return the decimal part of the number.

### Solution
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, decompose it into its integer and decimal parts.
    Return the decimal part of the number.

    Args:
        number (float): The input floating point number.

    Returns:
        float: The decimal part of the input number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Use the built-in math.floor function to get the largest integer smaller than the number
    from math import floor
    # Use subtraction to get the decimal part
    decimal_part = number - floor(number)
    return decimal_part
```

### Usage

```python
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
```
```
```
This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The decimal part is calculated by subtracting the largest integer smaller than the input number (obtained using `math.floor`) from the input number. The usage examples demonstrate how to call the function with different inputs.