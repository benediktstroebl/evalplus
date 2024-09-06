```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The code uses an intuitive approach that subtracts the largest integer smaller than the number to retrieve the leftover fraction. 

Here is a test case to test the function:
```python
assert truncate_number(3.5) == 0.5
```