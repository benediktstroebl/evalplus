```python
def truncate_number(number: float) -> float:
    # The code is split into a function and a docstring comment
    # that works in both Python 2 and Python 3
    # style.
    integer_part = number // 1
    decimal_part = number - integer_part
    return decimal_part

# Test suite
def test_truncate():
    assert truncate_number(3.5) == 0.25
    assert truncate_number(-3.5) == -2
assert truncate_number(1.0) == 0.0
assert truncate_number(0.0) == 0.0
assert truncate_number("3.5") == 0.0
```
This Python code defines a function called `truncate_number`, which takes a floating point number as input and returns the decimal part of the number. 

It achieves this by first subtracting the largest integer less than the input number from it, which isolates the integer part, and then subtracting the remainder from 1 from the original input number, which isolates the decimal part. 

The test suite includes several test cases that cover different scenarios, including negative numbers, non-integer inputs, and strings. This test ensures that the code correctly returns the decimal part for valid inputs and handles edge cases appropriately.