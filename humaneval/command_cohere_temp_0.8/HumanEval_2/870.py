```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input, and returns the decimal part of the number by subtracting the integer part of the number (obtained by converting number into integer). 

To test this function, you can call it with a float argument like so:
```python
 truncate_number(3.5)
# Expected output: 0.5
``` 
This will return 0.5, which is the decimal part of the number 3.5. 

This function can also be tested by comparing the result of the function call with the original input. This can be done using the following code:
```python
assert truncate_number(3.5) == 3.5 - 3 
# Expected output: True
``` 

This will result in True, indicating that the output of the function corresponds to the expected value.