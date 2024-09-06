```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # use python's built-in round function to round to integer
    integer = round(number)
    decimal = round(number - integer)

    return float(decimal)

# test cases
assert truncate_number(3.5) == 0.5
assert truncate_number(2.0) == 0.0
assert truncate_number(-0.5) == -0.0
assert truncate_number(0.0) == 0.0
assert truncate_number(1.0) == 1.0
assert truncate_number(1.25) == 1.25
assert truncate_number(2.3) == 2.3
assert truncate_number(2.1) == 2.1
assert truncate_number(4.5) == 3.5
assert truncate_number(7.9) == 4.9
```