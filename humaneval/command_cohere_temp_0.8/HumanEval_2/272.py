```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` itself, the int() function converts the float into an integer, leaving behind the remainder which is the requested decimal part of the number. 

Here is a test to ensure this function works properly:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(11.2) == 0.2
    assert truncate_number(2.0) == 0.0
```
This test suite contains four test functions that cover different cases, each test case checks if the output of the `truncate_number()` function is equal to the expected output. 
The assert statements assert the equality of these values, if the equality holds true, the test passes, otherwise, it fails and prompts you to pay attention to this test case. Do you have any further questions?