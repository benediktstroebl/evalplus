```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The function takes a floating point number as input and returns the decimal part of the number by subtracting the integer part of the number. 

Here is a test case to test the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.8) == 0.2
```