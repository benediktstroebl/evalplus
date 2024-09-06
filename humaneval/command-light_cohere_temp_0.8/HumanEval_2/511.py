```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Args:
        number (float): positive floating point number

    Returns:
        float: decimal part of the number
    """
    return 0.1 + (number - 1/10 **10)

# Test
print(truncate_number(3.5)) # Output: 0.1
print(truncate_number(1.1)) # Output: 0.1
print(truncate_number(1e100)) # Output: 4.1
print(truncate_number(1e-100)) # Output: 4.0
print(truncate_number(float('3'))) # Output: 3
```