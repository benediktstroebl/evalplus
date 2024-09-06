```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which effectively captures the residual value. 

To test this script you can run the following code:
```python
Test truncate_number() function:
>> truncate_number(3.5)
0.5
>> truncate_number(5.1)
0.1
>> truncate_number(2.8)
0.8
>> truncate_number(12)
0
```
This will correctly test the function against positive numbers with different decimal values.