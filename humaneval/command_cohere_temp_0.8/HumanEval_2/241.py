```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which yields the original number minus its integer part, which is the requested decimal part of the number. 

Here is a simple test suite that can be used to verify the functionality of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.7) == 0.7
    assert truncate_number(2.0) == 0.0
    assert truncate_number(10.2) == 0.2
``` 

To run the tests, you can simply call the function with different input values to verify that it returns the expected output. You can also incorporate these tests into a continuous integration (CI) framework to ensure that the function always behaves as expected.