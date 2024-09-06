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

The test will pass successfully, confirming the correct behavior of the `truncate_number` function. 
Let me know if you need any further assistance with any other related problems or explanations of the mechanics behind the answer!