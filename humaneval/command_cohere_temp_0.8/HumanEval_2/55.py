```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number and returns the result. 

To test this, try calling the function with the example provided in the prompt:
```python
truncate_number(3.5)
# Should return 0.5
```