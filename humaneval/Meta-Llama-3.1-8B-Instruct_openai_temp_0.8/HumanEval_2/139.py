### Truncate Number Decimal Part
#### Problem Statement

Given a positive floating point number, it can be decomposed into 
an integer part (largest integer smaller than given number) and decimals 
(leftover part always smaller than 1).

Return the decimal part of the number.

#### Solution

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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # Using the % operator to get the decimal part of the number
    decimal_part = number % 1
    return decimal_part
```
#### Usage Example

```python
# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.123))  # Output: 0.123
```

In this solution, the `%` operator is used to get the remainder of the division of the number by 1, which gives the decimal part of the number. This approach is straightforward and efficient.