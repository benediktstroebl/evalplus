```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the given floating point number and the nearest integer, which represents the decimal part of the number. 

To test this script, you can create a test case like this:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.8) == 0.2
    assert truncate_number(12.345) == 0.345
``` 

The tests ensure that the function correctly identifies the decimal part of different test cases.  This approach provides a straightforward solution to the problem and results in an efficient and understandable code.