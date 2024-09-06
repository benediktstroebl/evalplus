```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

Here is a test case to test the function:
```python
assert truncate_number(3.5) == 0.5
``` 
The code passes the test with flying colors!