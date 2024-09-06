```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which inherently truncates the decimal part of the number without any fancy calculations and gives you the output you are looking for. 

To test this, try invoking the function with the example provided in the prompt:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
This should yield the expected output of 0.5.