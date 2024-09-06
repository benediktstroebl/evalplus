```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which inherently excludes the integer part of the decomposition of the number, leaving behind the decimal part. 

Here is a simple test case to confirm the functionality of the script:
```python
truncate_number(3.5) == 0.5
```
The output of this test case is True, confirming the correct functionality of the script.