```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which inherently removes the largest integer part and leaves behind the residual fractional part. 

To validate the correctness of the implementation, one can simply print out the result of the function when called with the following input:
```python
print(truncate_number(3.5))
```
This will print:
```
0.5
```
Which confirms the correct operation of the function in producing the intended residual fractional part.  This approach is highly efficient with a time complexity of O(1) since it merely involves a single subtraction operation.