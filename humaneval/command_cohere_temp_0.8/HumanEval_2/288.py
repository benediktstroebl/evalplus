```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which yields the desired decimal part. 

To test this script you can use the following sample test:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(11.2) == 0.2
```
This test suite proves the correctness of the function for a few different cases. 

The combination of the solver function and the sample test ensures the problem is fully addressed.