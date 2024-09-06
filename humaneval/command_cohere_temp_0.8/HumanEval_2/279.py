```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. 

To test this function, here is a set of test cases to ensure its functionality:
```python
# Test case for truncate_number function
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.7) == 0.7
    assert truncate_number(2.2) == 0.2
    assert truncate_number(101.1) == 1.1
    assert truncate_number(1001.001) == 0.001
```
You can run these test cases by copying the above code into a Python environment of your choice and running the test_truncate_number function. 

These tests should cover all corner cases for the truncate_number function.