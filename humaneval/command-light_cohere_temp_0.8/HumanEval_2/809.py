```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    integer = (number // 1)
    return number - integer*1

# Test cases
print(truncate_number(3.5)) # Output: 2.0
print(truncate_number(-0.5)) # Output: -0.0
print(truncate_number(1.5)) # Output: 1.0
print(truncate_number(0.25)) # Output: 0.2
print(truncate_number(0.375)) # Output: 0.375
```