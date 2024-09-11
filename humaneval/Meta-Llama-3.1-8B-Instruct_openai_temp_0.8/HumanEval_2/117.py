### Truncating the Decimal Part of a Floating Point Number
```markdown
### Problem Statement

Given a positive floating point number, decompose it into its integer part and decimal part.

### Solution
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, decompose it into its integer part and decimal part.

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    return number - int(number)

### Example Use Cases
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.123))  # Output: 0.123
```
### Explanation

The `truncate_number` function takes a positive floating point number as input and returns its decimal part. The decimal part is obtained by subtracting the integer part of the number from the original number. In Python, the `int()` function truncates the decimal part of a floating point number and returns the integer part.

Note that this function assumes that the input number is positive. If the input number is negative, the function will return a negative decimal part which may not be the expected result. To handle negative numbers, additional logic would be required to determine the correct decimal part.

### Advice

For more complex problems, consider using libraries like `decimal` or `fractions` which provide support for precise arithmetic operations on floating point numbers. However, for simple problems like this one, the built-in `int()` function is sufficient.