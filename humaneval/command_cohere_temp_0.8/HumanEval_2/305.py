```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which inherently removes the largest integer part and leaves behind the residual fraction. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

result = truncate_number(test_truncate_number)
assert result == expected_output
```
The test case will fail if the result of truncate_number(test_truncate_number) does not equal to the expected output. 
This will ensure that the function behaves as expected, and will pass the test case for any float input. 
Feel free to add more test cases like this to increase test coverage and ensure correct function behaviour for different inputs. 
Let me know if you would like me to explain any of the steps outlined above!