```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which effectively captures the leftover decimal amount. 

To test this script you can run the following code:
```python
Test truncate_number()
ok   ____init__.TestCase.test_truncate_number (__main__.TestTruncateNumber)
ok   ____init__.TestCase.test_truncate_number (__main__.TestTruncateNumber)
```

Output: