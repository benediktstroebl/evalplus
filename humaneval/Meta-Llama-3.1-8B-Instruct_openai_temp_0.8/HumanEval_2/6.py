```markdown
### Truncating Decimal Part of a Number

#### Problem Description
Given a positive floating point number, decompose it into an integer part and decimals, and return the decimal part.

#### Solution
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)
```

#### Example Usage
```python
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

#### Explanation
The solution uses the fact that the decimal part of a number can be obtained by subtracting its integer part from the number itself. In Python, the `int()` function truncates the decimal part of a number, leaving only the integer part. Therefore, subtracting the integer part from the number gives the decimal part.
```