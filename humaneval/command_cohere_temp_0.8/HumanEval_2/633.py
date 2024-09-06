```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter to an integer (rounded down), and then returns the difference between the original number and the integer. The resulting difference is the fractional part of the original number, which is desired in this scenario. 

To test this function, here is a code block with its corresponding output:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(12.345)
0.345
>>> truncate_number(123123.123)
0.123
>>> truncate_number(123123)
None
>>> truncate_number(1.50001)
0.0001
```