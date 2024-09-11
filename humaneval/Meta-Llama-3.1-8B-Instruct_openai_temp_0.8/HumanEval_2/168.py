```markdown
### Truncate Number
#### Problem Description

Given a positive floating point number, it can be decomposed into
an integer part (largest integer smaller than given number) and decimals
(leftover part always smaller than 1).

Return the decimal part of the number.

#### Solution

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, return the decimal part.
    
    Args:
        number (float): A positive floating point number.
    
    Returns:
        float: The decimal part of the number.
    
    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.23))  # Output: 0.23
```

#### Explanation

To solve this problem, we use simple arithmetic to subtract the integer part of the number from the original number. The `int()` function in Python returns the largest integer smaller than the given number, effectively giving us the integer part. Subsequently, subtracting this integer part from the original number gives us the decimal part.