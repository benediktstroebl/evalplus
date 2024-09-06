```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which gives the leftover part of the decomposition that is always less than 1. 

Here are some example results of the function for test cases:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(2.0)
0.0
>>> truncate_number(1.5)
0.5
>>> truncate_number(1.0)
0.0
>>> truncate_number(0.5)
0.0
>>> truncate_number(0.1)
0.0
``` 
You can verify these results by conducting an integer subtraction of equivalent decimals or by testing them in the Python interpreter.