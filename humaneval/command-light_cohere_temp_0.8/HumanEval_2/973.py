```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    return n - int(n)

def test_truncate_number():
    assert truncate_number(3.5) == 0.5
   
    strategy:
        n = 3.5
        assert int(n) == 4
        assert truncate_number(1) == 0
        assert truncate_number(1.5) == 0.1
        assert int(n) == 2
        assert truncate_number(0) == 0
        assert truncate_number(-1) == -1
        assert truncate_number(float("INF")) == 0
        assert truncate_number(float("NaN")) == 0

This code defines a function `truncate_number` that takes a float number as input and returns the decimal part of that number. 

The function works by subtracting the largest integer less than the input number from it, which gives the integer part of the number. The largest integer is always smaller than the input number because it is less than or equal to it. 

The function then returns the remaining part of the number, which is always less than 1.