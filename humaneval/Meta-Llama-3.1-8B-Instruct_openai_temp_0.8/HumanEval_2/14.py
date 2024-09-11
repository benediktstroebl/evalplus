### Truncating Number to Decimal Part

Here's a simple Python script that defines and uses a function `truncate_number` to get the decimal part of a given number.

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


# Usage example:
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(4.23))  # Output: 0.23
    print(truncate_number(5.0))   # Output: 0.0
```

### Code Explanation

The `truncate_number` function takes a float number as an input and returns the decimal part of the number by subtracting its integer part from it. The integer part is obtained using the built-in `int` function, which truncates the decimal part.

### How to Run

1. Save this code in a file named `truncate_number.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the file using Python: `python truncate_number.py`
5. This will print the decimal part of the numbers `3.5`, `4.23` and `5.0`.