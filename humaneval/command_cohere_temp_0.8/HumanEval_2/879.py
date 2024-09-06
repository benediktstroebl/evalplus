```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which inherently truncates the number to the decimal part desired. 

To test this, try invoking the function with the example provided in the prompt:
```python
truncate_number(3.5)  # Expected to return 0.5
``` 
The output will indeed be 0.5, confirming the correctness of the function.