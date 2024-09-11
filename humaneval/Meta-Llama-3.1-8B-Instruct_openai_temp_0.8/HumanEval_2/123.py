```markdown
### Truncate a Number Script
#### Purpose
Given a positive floating point number, decompose it into an integer part and decimals, and return the decimal part.

#### Code
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Calculate the integer part using // operator which performs floor division
    integer_part = int(number // 1)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part
```

#### Usage
To use the `truncate_number` function, simply call it with a positive floating point number as an argument, like this:
```python
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.23))  # Output: 0.23
```

This script will work correctly for any positive floating point number as input.