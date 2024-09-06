```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` itself, the remainder is the decimal part of the number, and this is returned by the function. 

Here is a simple test case to verify the functionality of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(8.0) == 0.0
    assert truncate_number(2.8) == 0.1
``` 

The assert statements will check if the output of the `truncate_number` function is correct for the respective input values.