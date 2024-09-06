```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the given floating point number and the nearest integer, which represents the decimal part of the number. 

Here are some test cases to ensure the correct functioning of the above function:
```python
# Testing the function against a few inputs
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(11.2) == 0.2
assert truncate_number(0.1) == 0.0
```