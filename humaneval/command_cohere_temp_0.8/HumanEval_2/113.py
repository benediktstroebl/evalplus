```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which effectively captures the leftover decimal amount. 

To test this, try calling the function with the example provided in the prompt:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
This will return 0.5, which is the expected output.