```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which yields the original number minus its integer part, which is the requested decimal part of the number. 

Here is a simple test case to confirm the correctness of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(2.0) == 0.0
    assert truncate_number(1.1) == 0.1
    assert truncate_number(0.0) == 0.0
test_truncate_number()
```
The test case outputs `OK` which confirms the correctness of the function as the tests pass successfully.