```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the floor of the input number. This difference is the leftover part that the prompt describes, so returning this difference guarantees returning the desired decimal part of the number. 

Here is a test case that can be used to verify the functionality of the code:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(12.83) == 0.83
```
This test suite uses the Python assert statement to verify that the output of the truncate_number function is correct for a variety of input values.