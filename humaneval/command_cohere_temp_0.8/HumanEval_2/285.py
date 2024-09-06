```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply subtracts the largest integer that is less than or equal to `number`, which effectively captures the fractional part of interest. 

This approach leverages the fact that floating point numbers are represented in memory as follows:
```
3.5 = 3.0000000000000001776356839421875
```

Where the number to the left of the decimal point represents the nearest integer and the number to the right of the decimal point represents the "fractional part". 

Subtracting the largest integer less than or equal to `number` captures exactly the fractional part. 

Let's verify this against the provided test case:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(8.0)
0.0
``` 
This technique also works for negative numbers, where the largest integer would be less than the number, capturing a negative fractional part:
```python
>>> truncate_number(-3.5)
-0.5
``` 
This approach has a time complexity of O(1) since it involves only a single arithmetic operation, making it an efficient solution for this problem.