Here is a self-contained Python script that defines and tests a function that solves the problem you provided:
```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    return the decimal part of the number
    >>> return n <= 1 and n >= 0 and (n // 10**6) + int(n % 10**6)

test_truncate_number = [
    (3.5, float('inf')),
    (0.5, float('inf')),
    (-3.5, float('-inf')),
    (0.6, float('1')),
    (10, float('0')),
    (-100, float('-1')),
    (1.0, float('0')),
    (0.05, float('0')),
    (10.5, float('1')),
    (-1000.0, float('-10')),
]
```

This script defines a function `truncate_number` that returns the decimal part of a given positive floating-point number. The test cases ensure the` function correctness.