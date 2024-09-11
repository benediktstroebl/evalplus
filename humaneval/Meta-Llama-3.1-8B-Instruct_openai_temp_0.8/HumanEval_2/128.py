### Truncating Decimal Part of a Number

The following Python script defines a function `truncate_number` to calculate the decimal part of a given positive floating point number.

```markdown
### truncate_number.py

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


if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.23))  # Output: 0.23
```

### Explanation

The `truncate_number` function works by subtracting the integer part of the number from the number itself. This leaves only the decimal part.

In the example script, we have a docstring that explains what the `truncate_number` function does, its parameters, and its return value. We also include examples of how to use the function.

Finally, we have a `main` block that demonstrates how to use the `truncate_number` function with some example inputs.
```