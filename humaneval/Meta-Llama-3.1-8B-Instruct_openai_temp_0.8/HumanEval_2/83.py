```markdown
### Truncate Decimal Part of a Number

This Python script defines a function `truncate_number` that takes a positive floating-point number as input and returns its decimal part.

#### Code
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    >>> truncate_number(3.5)
    0.5
    
    Parameters:
    number (float): A positive floating-point number.
    
    Returns:
    float: The decimal part of the number.
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

#### Explanation
The function uses the fact that subtracting the integer part of a number from the number itself leaves the decimal part.
In Python, we can extract the integer part of a number using the `int()` function, which converts a number to an integer by truncating its decimal part.
Therefore, subtracting the integer part from the number itself yields the decimal part.