```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer less than or equal to the given number, as represented by the integer `int(number)`. This subtraction operation effectively removes the integer part of the decomposition, leaving behind the desired decimal part. 

This function's simplicity and directness make it highly efficient, capable of executing the truncation process in a single line of code.