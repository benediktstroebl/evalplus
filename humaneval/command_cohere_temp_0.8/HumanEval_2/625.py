```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

To test this script, you can copy and paste it into a Python environment or IDE, and it should pass the test case provided in the original prompt, as well as any other test case you may want to add for validation.