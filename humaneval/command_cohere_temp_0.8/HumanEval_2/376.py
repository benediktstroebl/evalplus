```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which effectively captures the leftover part and returns it. 

To validate the operation, please consider running this basic test:
```python
>> truncate_number(3.5)
0.5
>> truncate_number(8.0)
0.0
>> truncate_number(2.5)
0.5
``` 
The above test case confirms that the function appropriately identifies the decimal component of different numbers. 
If you encounter any uncertainties or require additional clarification, don't hesitate to ask!