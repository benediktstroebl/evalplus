```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which effectively captures the residual value. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_result = 0.5

result = truncate_number(test_truncate_number)

assert result == expected_result
```

The test code checks if the result of the function corresponds to the expected result. 
If the outcome of the function is 3.5 - 3 = 0.5, then the test will pass. 
This will validate the correctness of the function. 
It is important to note that in this case, the decimal part of the number is considered to be the part of the number that is less than 1. 
This is consistent with the prompt, however, it is important to be aware of this assumption when considering different types of input.