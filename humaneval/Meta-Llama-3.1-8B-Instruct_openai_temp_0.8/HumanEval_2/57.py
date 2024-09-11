```markdown
### Truncate Number Function

#### Problem Description

Given a positive floating point number, it can be decomposed into 
an integer part (largest integer smaller than given number) and decimals 
(leftover part always smaller than 1).

Return the decimal part of the number.

#### Code
```python
def truncate_number(number: float) -> float:
    """
    Returns the decimal part of a given positive floating point number.

    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    return number - integer_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.23))  # Output: 0.23
```

#### Explanation

This function works by first converting the input number to an integer using `int(number)`. This integer is the largest integer smaller than the input number, which represents the integer part of the number.

The decimal part is then calculated by subtracting the integer part from the input number.

The function returns this decimal part.