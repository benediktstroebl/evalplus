```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the given floating point number and the nearest integer, which represents the decimal part of the number. 

Here are some test cases to verify the correctness of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.8) == 0.8
    assert truncate_number(0.1) == 0.0
    assert truncate_number(11.2) == 0.2
    assert truncate_number(123.456) == 0.456
    assert truncate_number(1.5) == 0.5
    assert truncate_number(157.3) == 0.3
test_truncate_number()
``` 
The nearest integer value is obtained using the built-in `int()` function, and the difference between the original number and the integer part is the decimal part, which is then returned.