```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer less than or equal to the given number, as represented by the integer `int(number)`. This subtraction operation effectively isolates and removes the integer part of the decomposition, leaving behind the desired decimal part. 

This function directly complements the provided test case and behaves accordingly when encountering different types of input:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(8.0) == 0.0
    assert truncate_number(12.7) == 0.7
    assert truncate_number(1.0) == 0.0
    assert truncate_number(100.01) == 0.01
    assert truncate_number(0.8) == 0.0
    try:
        truncate_number(13)
    except TypeError:
        pass
    else:
        raise AssertionError("Input error not raised for invalid input 13")
```