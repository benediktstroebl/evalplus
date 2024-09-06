```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)
```

The function takes a `number` as input, which is a positive floating point number, and returns the decimal part of the number. It does so by taking two integers, the given number `n`, and the largest integer smaller than `n`, which is denoted by `int(n)`. The difference between these two integers is the leftover part, which is always smaller than 1 and therefore constitutes the decimal part of `n`. 

Here is a test case that verifies the correct functionality of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(12.8) == 0.8
``` 

This test case covers three different scenarios in which the function is provided with different positive floating point numbers, and it checks whether the output corresponds to the decimal part of the number provided.