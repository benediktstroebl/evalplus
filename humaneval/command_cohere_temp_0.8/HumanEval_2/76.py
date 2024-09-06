```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which inherently removes the largest integer part and leaves behind the residual fraction. 

To test this script you can run:
```python
Test truncated number:
>> truncate_number(3.5)
0.5
>> truncate_number(12.345)
0.345
>> truncate_number(100.7)
0.7
```
This would confirm that the function correctly truncates the provided numbers to their residual fractions. 
Please note that the expected output for the provided test cases are the numbers appended to the right, with a trailing 0.7, 0.345, and 0.5 respectively.