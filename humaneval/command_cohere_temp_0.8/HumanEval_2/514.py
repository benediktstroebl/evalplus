```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which inherently removes the largest integer part and leaves behind the residual fraction. 

To validate the correctness of the implementation, one can simply test it against the provided test case:
```python
>>> truncate_number(3.5)
0.5
```
The code passes this test case and yields the desired output.