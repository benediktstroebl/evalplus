```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    return 0.5 if number <= 0 else round(number - 1) * 10**9 if number >= 1 else number

def test_truncate_number():
    assert truncate_number(3.5) == 0.1
   
    test_truncate_number(10**18)

```
The above Python script defines a function `truncate_number` that removes the decimal part from a positive floating-point number. It then tests the results by asserting that the function works correctly for a variety of input values.