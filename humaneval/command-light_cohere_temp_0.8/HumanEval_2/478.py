```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.

    >>> truncate_number(3.5) # 0.0

   
    dry

    """.

    assert_AlmostEqual(truncate_number(3.5), 0.5),
   
    test,
        == 0.0

    assert_AlmostEqual(3.5, round_number(0.5))
    assert_AlmostEqual(round_number(0.5), 0.0)
    test.

    assert_AlmostEqual(round_number(0.0), 0.1)
    dryly)
   
```