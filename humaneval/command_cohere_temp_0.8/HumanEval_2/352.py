```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the total number, returning the desired decimal part. 

To test this script, you can call the `truncate_number` function with a floating point input, such as `3.5`. The function should return `0.5`. 
This function works for positive numbers less than 1 as well, e.g., `0.5` will return `0.0`. 
However, it will not work correctly for numbers less than 1, like `0.2`, where the integer part will be 0, and the difference will be a negative number. Adjustments can be made to the logic to account for this if necessary.