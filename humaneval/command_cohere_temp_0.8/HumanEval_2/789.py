```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the decimal part of the number. 

To test this function, you can call it with a floating point input and verify that the returned value is less than or equal to 1. Here is an example:
```python
assert truncate_number(3.5) == 0.5
assert truncate_number(2.0) == 0.0
assert truncate_number(1.5) == 0.5
assert truncate_number(1.0) == 0.0
``` 

These tests check four different inputs, including one edge case where the input is equal to an integer, and verify that the output is as expected.