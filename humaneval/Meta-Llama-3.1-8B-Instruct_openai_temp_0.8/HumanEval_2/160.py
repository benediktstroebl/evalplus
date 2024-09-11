### Truncate Number Function
#### Description
This Python script defines a function `truncate_number` that takes a positive floating point number and returns its decimal part.

#### Code
```markdown
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

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Ensure the input is a positive number
    if number <= 0:
        raise ValueError("Input must be a positive number")

    # Subtract the integer part from the number
    decimal_part = number - int(number)
    
    # Return the decimal part
    return decimal_part
```

#### Example Use Cases

```python
# Test the function with a positive floating point number
print(truncate_number(3.5))  # Output: 0.5

# Test the function with a negative number
try:
    print(truncate_number(-3.5))
except ValueError as e:
    print(e)  # Output: Input must be a positive number

# Test the function with a non-numeric input
try:
    print(truncate_number('a'))
except TypeError:
    print("Input must be a number")
```

This script defines a function `truncate_number` that calculates the decimal part of a given positive floating point number. It includes input validation and example use cases to demonstrate its usage.