```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input and returns the decimal part of the number by subtracting the integer part of the number (obtained by rounding down the input value) from the input number. The markdown code example provided essentially defines the same function but with more comments and a usage example. 

This function is a straightforward way to handle this particular use case, but in some cases, it might be desirable to separate the decimal and integer parts of a number using a different approach. 

Here is a test case that can be used to verify the correct operation of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.99) == 0.01
```