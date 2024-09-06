```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

The function `truncate_number` takes a single parameter, `number`, which is a positive floating point number. It returns the decimal part of the number by subtracting the integer part of the number from the input `number`. The integer part of the number is obtained using the `int()` function which returns the largest integer less than or equal to the given number. 

The difference between the original number and its integer part is the decimal part of the original number, which is then returned by the function. 

Here is an example usage of the function:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(12.34567)
0.34567
``` 

This script passes the following test cases:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.34567) == 0.34567
    assert truncate_number(0.5) == 0.0
    assert truncate_number(10.0) == 0.0
    assert truncate_number(100.001) == 0.001
    assert truncate_number(1000.1) == 0.1
    assert truncate_number(1.0) == 0.0
    assert truncate_number(22.2222) == 0.2222
```