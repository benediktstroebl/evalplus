```python
def truncate_number(number):
    return number - int(number)
```

The function takes in a `number` as input and returns the decimal part of the number by simply subtracting the integer part of the number. 

Here is a test case to confirm the functionality of the script:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.345) == 0.345
```