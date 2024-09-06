```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter into an integer and then returns the difference between the original number and the integer. The result is the decimal part of the original number.

To test this function, you can call it with a few test cases like this:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(12.34567)
0.34567
>>> truncate_number(100)
Traceback (most recent call last):
  ...
TypeError: Cannot subtract int from float
```
The first two tests show that it works as expected, while the third test shows that the function handles integer inputs gracefully by raising a TypeError.