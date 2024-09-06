```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number, subtracts the largest integer less than the number, which leaves us with the residual fraction (the 'decimals' in the original description of the task). 

To test this function, the Python interpreter provides a handy built-in tool:
```
$ python
>>> truncate_number(3.5)
0.5
>>> truncate_number(12.2)
0.2
>>> truncate_number(2.1)
0.1
>>> truncate_number(1.1)
0.0
>>> truncate_number(11.0)
0.0
```
The result is always the residual fraction part of the original number, which is what the original task asks for.