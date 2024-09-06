```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number
    >>> return 0.5 if number <= 5
   0
    > return 0
    <-- Truncate the number
    integer part = int(number)
    decimal part = number - integer part
    return decimal part
    """

# Test case 1:
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
   
# Test case 2:
assert truncate_number(5) == 1.5
# Test case 3:
assert truncate_number(1.25) == 0.25
# Test case 4:
assert truncate_number(-5) == -1.25
# Test case 5:
assert truncate_number(-3.75) == -00.75
# Test case 6:
assert truncate_number(-1) == -1
```

This Python function called `truncate_number` takes a single argument, which is a positive floating-point number. The function returns the decimal part of the number, which is the difference between the number and its largest integer less than or equal to it.

The function uses the built-in function `int` to extract the integer part of the number, and then subtracts this integer part from the number to get the decimal part.

The function then returns the decimal part of the number.

In this script, we have created a test suite with several test cases to verify the correctness of the `truncate_number` function.