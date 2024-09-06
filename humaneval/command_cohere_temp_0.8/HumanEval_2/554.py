```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which effectively captures the residual value. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

result = truncate_number(test_truncate_number)
assert result == expected_output
```

The test code checks if the output of the function is equal to the expected output when given the input `3.5`. 
The `assert ` statement checks if the result of the function is equal to the expected output. If it is, the test passes, and the output is printed out. If it isn't, the test fails, and the specific differences between the expected and actual values are highlighted, helping developers understand what went wrong and how to fix it.