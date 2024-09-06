```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer less than or equal to the given number, as expressed by the expression `int(number)`. This effectively removes the integer part of the number, leaving only the decimal part. 

Here are some example outcomes of the function for different input values:
- For `truncate_number(3.5)`, the output is `0.5`. The integer part of `3.5` is `3`, and the remaining `0.5` is the decimal part. 
- For `truncate_number(2.8)`, the output is `0.8`. The integer part of `2.8` is `2`, and the remaining `0.8` is the decimal part. 
- For `truncate_number(5.0)`, the output is `0.0`. The integer part of `5.0` is simply `5`, and the decimal part is `0.0`. 

These examples demonstrate how the function extracts the decimal part of various input numbers and returns it as the output.