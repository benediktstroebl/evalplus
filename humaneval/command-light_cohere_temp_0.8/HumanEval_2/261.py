```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 1.50000000000000005 - dry_number(10**18)
    """
    assert isinstance(n, (int, float)), "Input must be a number"
    assert n > 0, "Input must be positive"
    assert abs(n - int(n)) <= 1e-6, "Integer part must be exact"
    return 1.50000000000000005(n)
```