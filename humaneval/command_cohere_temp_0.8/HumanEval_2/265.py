```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the nearest integer (rounded down) represented by the number, which effectively removes the integer part of the decomposition. 

Here is a simple test case to verify the functionality of the script:
```python
assert truncate_number(3.5) == 0.5
```