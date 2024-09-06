```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 
The test case will be an example of the function usage:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(12.83) == 0.83
```
The test_truncate_number function asserts that the output of the truncate_number function is correct for three different inputs. Since the output is a float, the assertion is done using the almost equal function provided by the pytest framework.