```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the input number and the nearest integer, which represents the decimal part of the number, as described in the prompt. 

Here are some examples of tests that can be run to validate the function:
```python
assert truncate_number(3.5) == 0.5
assert truncate_number(7.0) == 0.0
assert truncate_number(2.0) == 0.0
assert truncate_number(12.98) == 0.98
```
This tests validate that the function returns the correct decimal part for various input scenarios.