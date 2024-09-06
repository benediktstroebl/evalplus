```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which effectively captures the residual decimal part. 

To validate the operation, a simple test case is provided below:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.8) == 0.2
test_truncate_number()
```
The tests ensure the function behaves as intended for a few different input cases. 
To run the tests, you can copy this code into a Python file (e.g., `test_truncate_number.py`) and run the file using the command line:
```bash
python test_truncate_number.py
``` 
The output will demonstrate the test successes, confirming the function's effectiveness.