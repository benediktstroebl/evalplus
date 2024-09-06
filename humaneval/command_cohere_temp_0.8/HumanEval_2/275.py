```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function simply takes the parameter and subtracts the largest integer 
less than the parameter. 
The above solution assumes that the number is positive or zero. If the number 
is negative, the same approach can be taken by ignoring the sign. 

The unit tests for this function could be:
```python
def test_truncate_number():
    assert truncate_number(1.5) == 0.5
    assert truncate_number(2.7) == 0.7
    assert truncate_number(3.0) == 0.0
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.83) == 0.83
    assert truncate_number(-1.5) == -0.5
    assert truncate_number(-2.7) == -0.7
    assert truncate_number(-3.0) == -0.0
    assert truncate_number(-3.5) == -0.5
``` 
The assert statements in the test function check that the output of `truncate_number` is correct. 
The tests cover both positive and negative numbers as well as numbers with different numbers of digits after the decimal point. 
They ensure that the function follows the specification of returning the decimal part of the number.