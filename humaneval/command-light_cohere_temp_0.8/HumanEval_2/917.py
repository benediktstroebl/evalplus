```python
def truncate_number(n):
    """Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: The decimal part of the number.
    return: float('0')/n if n<1 else n
    """

def test_truncate_number():
    try:
        x = 3.5
        y = truncate_number(x)
        assert y == 0.5
        raise AssertionError
   
print("Test passed!")

```