```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the input `number` and returns the result, which is the decimal part of the number. 

Here is a test case to verify the correct operation of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.345) == 0.345
```