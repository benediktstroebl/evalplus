```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which inherently truncates the number to the decimal part alone, which is the desired output.

To test this function, here is a markdown code block with the corresponding test code:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.7) == 0.7
    assert truncate_number(0.1) == 0.0
    assert truncate_number(101.1) == 0.1
    assert truncate_number(1005.2) == 0.2
```
This test suite contains itests that cover various cases of the truncate_number function.