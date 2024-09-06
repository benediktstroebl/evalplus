```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single argument, `number`, which is expected to be a positive floating point number. It returns the decimal part of the number by subtracting the integer part of the number. The integer part of a number is the largest integer that is less than or equal to the given number. 

Here is an example of using the above function:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(12.345)
0.345
```