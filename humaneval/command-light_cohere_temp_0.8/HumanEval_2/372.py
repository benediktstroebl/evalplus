```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number
    """
    number += 1  # Add 1 to ensure positive number
    return 10 ** (number // 10) - number % 10  # Apply logarithm and formula to get decimal part

# Test cases:
 assert truncate_number(3.5) == 0.4
 assert truncate_number(-3.5) == -0.00
 assert truncate_number(0) == 0
 assert truncate_number(-0) == 0
 assert truncate_number(1) == 1
 assert truncate_number("3.5") == 0.4
 assert truncate_number(10) == 1.0
 assert truncate_number(14.1) == 1.6
 assert truncate_number(0.9) == 0.7
 assert truncate_number(-14.2) == -0.5
 assert truncate_number(300.3) == 2.7
 assert truncate_number(0.00001) == 0.00001
```