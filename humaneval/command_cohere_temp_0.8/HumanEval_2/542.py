```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 
The test case will look like:
```python
test_truncate_number = '''
>>> truncate_number(3.5)
0.5
>>> truncate_number(12.34567)
0.34567
>>> truncate_number(100)
Traceback (most recent call last):
  ...
TypeError: Argument must be a non-integer number
'''
```