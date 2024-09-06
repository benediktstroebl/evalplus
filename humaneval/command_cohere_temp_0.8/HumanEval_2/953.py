```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which inherently removes the integer part of the number and leaves behind the residual decimal part. 

To validate the correctness of the implementation, one can conduct some spot checks like so:
```python
# Testing the Function
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(0.4) == 0.0
``` 
This will help assure that the function is returning the expected outputs.