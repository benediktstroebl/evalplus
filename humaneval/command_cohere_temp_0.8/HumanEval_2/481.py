```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which yields the original number minus its integer part, which is the desired decimal part of the number. 

Here is a simple test case to confirm the functionality of the function:
```python
assert truncate_number(3.5) == 0.5
```