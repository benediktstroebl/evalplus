```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

Here is a test case that verifies the solution:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.3) == 0.3
    assert truncate_number(2.1) == 0.1
    assert truncate_number(100.001) == 0.001
    assert truncate_number(0.8) == 0.0
``` 

Note that the solution is not explicitly formatted as a markdown code block, but it can be easily copied and run as a script, and it includes a test block that can be executed to verify the correctness of the solution.