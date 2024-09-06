```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which effectively captures the residual decimal part. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_result = 0.5

result = truncate_number(test_truncate_number)

assert result == expected_result
```
The test case would look for an assert statement that verifies the correctness of the computed result. 
If desired, the following code can be used to introduce a separate testing module: 
```python
# testing module
def test_truncate_number():
    test_truncate_number = 3.5
    expected_result = 0.5
    result = truncate_number(test_truncate_number)
    assert result == expected_result
``` 
This way the result of the computation would not be overwritten. 
Running the test case would look like this:
```python
python test_truncate_number.py
``` 
This approach is commonly used in testing frameworks to isolate and verify the correctness of different functions.