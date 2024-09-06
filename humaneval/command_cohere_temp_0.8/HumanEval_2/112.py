```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 

Here is a test case to test the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.9872) == 0.9872
    assert truncate_number(123123.123) == 0.123
test_truncate_number()
```