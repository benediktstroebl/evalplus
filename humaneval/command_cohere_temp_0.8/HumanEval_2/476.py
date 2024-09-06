```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the given floating point number and the closest integer to it, which corresponds to the decimal part of the number. This difference is always less than 1, and therefore is the desired result. 

To test this function, you can call it with any floating point input, and compare the output to the original number to verify that they differ only by a difference less than 1. For example:
```python
test_cases = [3.5, 7.777, 123.456, 1.0, 0.4999]
for case in test_cases:
    assert abs(truncate_number(case) - case) < 1
```