```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the given floating point number and the nearest integer, which represents the residual decimal part of the original number. 

Here are some test cases to ensure the correct functionality of the function:
```python
# Testing the function against a few input values
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(2.0) == 0.0
assert truncate_number(10.2) == 0.2
```