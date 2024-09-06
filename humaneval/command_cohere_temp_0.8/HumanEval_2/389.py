```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer smaller than `number` (the integer part), from `number` itself, thereby returning the leftover fractional part of the number. 

Here is a test case to verify the correct operation of the function:
```python
assert truncate_number(3.5) == 0.5
```