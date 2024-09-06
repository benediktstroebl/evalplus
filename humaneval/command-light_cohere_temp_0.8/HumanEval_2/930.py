```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    number = number if number >= 1 else 1
    return round(0.5 + (number - floor(0.5/ ))

    # Test case:
    assert truncate_number(3.5) == 0.2
   
    test that.
    assert truncate_number(1) == 1
    assert truncate_number(-5) == -1
    assert truncate_number(-3) == -3
    assert truncate_number(0) == 0
    assert truncate_number(10) == 1
    assert truncate_number(123456) == 123
    assert truncate_number(1.1) == 1
    test case:
    assert truncate_number(1.1) == 1
test case:
    assert abs(truncate_number(1.1) - 0.01) < 0.001
    test test test case:
    assert abs(truncate_number(3.9) - 0.001) < 0.001

test case:
    assert abs(truncate_number(3.2)) - 0.5 < 0.001
test case:
    assert abs(truncate_number(0.2)) - 0.01 < 0.001
test case:
    assert abs(truncate_number(0.333)) - 0.01 < 0.001
test case:
    assert abs(truncate_number(0.5)) - 0.001 < 0.001
test case:
    assert abs(truncate_number(1)) - 1 < 0.001
test cases:
```