```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which effectively captures the residual/decimal part of the decomposition. 

To test this, try calling the function with the example provided in the prompt:
```python
truncate_number(3.5)  # Returns 0.5
``` 
This output matches the example in the problem statement. 

I hope this solves your problem. Let me know if you have any additional questions or if you'd like me to help out with any other coding problems or topics you'd like to explore!