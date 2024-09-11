```markdown
### Truncate Number Function

This function truncates a given positive floating point number into its decimal part.

#### Code

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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Example usage
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.2))  # Output: 0.2
```

#### Explanation

This function works by subtracting the integer part of the number from the original number itself. The `int(number)` function truncates the decimal part, leaving only the integer part. Therefore, `number - int(number)` effectively returns the decimal part of the number.

Note: This function assumes that the input number is positive. If you want to handle negative numbers, you will need to adjust the function accordingly.