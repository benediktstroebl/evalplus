```python
def truncate_number(n: float) -> float:
    """
    Convert the float number into the integer part and decimal part
    Returns: tuple containing integer part and decimal part
    """
    return (int(n < n**0.5), decimal,n) / n**0.5)

def test_truncate_number():
    assert truncate_number(3.5) == (0, 5)
```
This Python script defines a function `truncate_number` that splits a positive floating point number into its integer and decimal parts, and returns a tuple of these two components. It also includes a test function `test_truncate_number` that checks the correctness of the `truncate_number` function using the provided test case.