```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function simply subtracts the integer part of the number from the initial number provided, as the leftover would be the decimal part they want to extract. 

To test this, you can call the function with the example provided above with `truncate_number(3.5)` and it should return `0.5`.