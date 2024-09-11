Here's a self-contained Python script that solves the problem:

```markdown
### Truncating Decimal Part of a Floating Point Number

#### Code

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    :param number: A positive floating point number
    :return: The decimal part of the number
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
```

#### Explanation

The `truncate_number` function takes a positive floating point number as input, subtracts its integer part (obtained using the `int()` function), and returns the decimal part. This works because the integer part of a number is always the largest integer that is less than or equal to the number, so subtracting it from the original number leaves only the decimal part.