```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 
The test cases will look as follows:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.7) == 0.7
    assert truncate_number(2.2) == 0.2
    assert truncate_number(123.456) == 0.456
    assert truncate_number(1001.1) == 0.1
``` 
The code above tests different numbers to see if the output of the `truncate_number()` function is correct.