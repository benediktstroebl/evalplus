```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the floor of the input number. This difference is the leftover part that the prompt speaks of and is always less than 1. The function returns this difference, which is the decimal part of the number. 

Here is a simple test case to confirm the functionality of the code:
```python
assert truncate_number(3.5) == 0.5
``` 
The code passes this test and returns the expected value. 

If you need more test cases, please let me know!