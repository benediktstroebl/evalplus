```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Return the decimal part of the number, or 0.0 if n is positive.

    >>> test_truncate_number(10.0)
   
    test_truncate_number(10.0)
   
    print("10.0 decimal part:", truncate_number(10.0))
    test_truncate_number(0.5)
    print("0.5 decimal part:", truncate_number(0.5))
    test_truncate_number(-10.0)
print("Negative number:", truncate_number(-10.0))
```