```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which inherently removes the largest integer part and leaves behind the residual fractional part. 

To validate the correctness of the implementation, one can compare it with the result of subtracting the largest integer less than or equal to `1e-9` from `1e-9` to verify that the function returns `0`, which signifies the removal of all integer parts down to the precision of 1e-9. 

To test for correctness with a larger margin of error, one can evaluate the function with `0.99` and confirm that it returns `0.01`. 

These tests help verify that the function accurately removes the integer part of the given number and returns the desired decimal part.