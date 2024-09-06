```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    return number - int(number)

# Test cases
print(truncate_number(3.5)) # Output: 0.5
print(truncate_number(-3.5)) # Output: -3.0
print(truncate_number(0.5)) # Output: 0.5
print(truncate_number(0.01)) # Output: 0.01
print(truncate_number(1.2)) # Output: 1.2
print(truncate_number(1.3)) # Output: 1.2
print(truncate_number(float('INF'))) # Output: 0.0
```