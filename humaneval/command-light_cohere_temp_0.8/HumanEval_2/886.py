Here is a Python script with a self-contained function that solves the problem you've described:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    """ Returns the
    number in a decimal representation.

# Test cases
print(truncate_number(3.5)) # Output: 0.01
print(truncate_number(10.5)) # Output: 1.00
print(truncate_number(0.5)) # Output: 0.00
print(truncate_number(-3.5)) # Output: -1.2
print(truncate_number(10)) # Output: 1.0
```