```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as input and returns the decimal part of the number. It does so by taking the difference between the input number and the largest integer less than or equal to the input number, as represented by the integer `int(number)`. This subtraction operation effectively removes the integer part of the number, leaving behind the decimal part, which is then returned as the result. 

This function directly computes the decimal part without explicitly needing to consider the separation of the number into an integer part and a decimal part.