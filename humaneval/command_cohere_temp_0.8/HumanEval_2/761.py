```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the given floating point number and the closest integer to it, which represents the decimal part of the number. 

To test this script, you can create a test case like this:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.8) == 0.2
```

The provided function adheres to Python's syntax and conventions for a stand-alone script. If you're integrating this function within a larger code base, you might consider incorporating error handling, documentation, and more robust testing for assurance of functionality.