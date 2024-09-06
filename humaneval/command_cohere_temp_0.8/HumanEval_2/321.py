```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single parameter, `number`, which represents the positive floating point number to be truncated. It returns the decimal part of the number by subtracting the integer part. The integer part is obtained by converting the number to an integer using `int()`, and then the decimal part is obtained by subtracting this integer value from the original number. This effectively removes the integer component, leaving only the decimal portion. 

To validate the behavior of the code, you can write a test case that ensures the function returns the expected value for a specific input:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(2.0)
0.0
```