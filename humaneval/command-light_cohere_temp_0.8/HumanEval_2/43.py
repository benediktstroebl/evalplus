```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number.

    Example integer part = round(n // 1e9)
    decimal part = n - integer part
    return decimal_part

# Test the function
assert truncate_number(3.5) == 0.2
assert truncate_number(0.5) == 0.1
assert truncate_number(-1.1) == -0.1
assert truncate_number(1.0) == 1.0
assert truncate_number('123.1') == 1.1
assert truncate_number('1.5') == 0.3
assert truncate_number('1.9') == 1.0
```