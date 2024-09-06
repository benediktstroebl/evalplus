```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which yields the original number minus its integer part, which is the requested decimal part of the number. 

Here is a simple test case to confirm the functionality of the function:
```python
assert truncate_number(3.5) == 0.5
``` 
The `assert` statement will confirm that the function returns the correct value. 

This approach is the simplest and most straightforward to solve the problem, however, it is worth noting that it is prone to potential numerical accuracy issues.