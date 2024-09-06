```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` itself, leaving behind the residual fraction. 

To test this, try calling the function with the example provided in the prompt:
```python
truncate_number(3.5)
# Should print: 0.5
```