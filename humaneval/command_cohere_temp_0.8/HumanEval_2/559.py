```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 
The function int(number) returns the largest integer that is less than or equal to the input number, and the result of subtracting int(number) from number is equal to the "leftover part" (i.e., the fractional part), which is always less than 1.