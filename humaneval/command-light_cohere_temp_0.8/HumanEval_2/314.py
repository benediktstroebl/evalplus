```python
def truncate_number(n):
    """Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    return round(n - int(n))

# Test cases
assertEqual(truncate_number(3.5), "0.5")
assertEqual(truncate_number(-3.5), "0.5")
assertEqual(truncate_number(0.5), "0")
assertEqual(truncate_number("3.5"), "0")
assertEqual(truncate_number("1.01"), "1")
assertEqual(truncate_number("0.9"), "0")
assertEqual(truncate_number("1.2"), "1")
```