```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single argument, `number`, which is expected to be a positive floating-point number. It uses the subtraction operation (`-`) to subtract the integer part of the number from the given number. The integer part of a number is the largest integer that is less than or equal to the number. 

For example, in the call `truncate_number(3.5)`, 3 is the integer part of 3.5, so the function returns 0.5.