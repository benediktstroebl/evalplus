```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, yielding the decimal part, then returns this value. 

To test this script, you can call the function with the input `3.5`, and compare the output (`0.5`) to the expected output. 
```python
truncate_number(3.5) == 0.5
```
The output of this comparison should be `True`.