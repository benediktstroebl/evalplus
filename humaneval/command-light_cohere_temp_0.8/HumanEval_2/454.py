```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.1 if number <= 1 else number % 1 if number > 1 else number
    """

def test_truncate_number():
    assert truncate_number(3.5) == 0.1
    print("passes!")
def test_second():
    assert truncate_number(5) == 1
    assert truncate_number(7) == 7
    assert truncate_number(10) == 1
    assert truncate_number(100) == 2.5
```

The above code defines a function that takes a float number as input and returns the decimal part of that number. It uses a simple logic to return 0.1 if the number is less than or 1 if it's greater than 1, else it returns the number itself.