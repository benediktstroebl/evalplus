```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter to an integer (via int(number)) and then returns the difference between the original number and the integer (via number - int(number)), which is the residual decimal part the task is asking for. 

To test this script, you can call the function with the argument 3.5, which will return 0.5 -- the decimal part of the number:
```python
truncate_number(3.5)
```
The output will be: 0.5