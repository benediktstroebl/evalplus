```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The function `truncate_number` returns the decimal part of the input `number` by subtracting the integer part of `number`. 

Here is a test case to check if the function works as intended:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(12.83) == 0.83
```

Surely, feel free to add more test cases to cover other scenarios! Let me know if you would like me to make any modifications to the script. I am here to assist you!