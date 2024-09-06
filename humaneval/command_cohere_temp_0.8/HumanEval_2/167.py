```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the floor of the input number. This difference is the leftover part that the prompt is asking for. 

To validate this solution, one could write a test like this:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(2.5)
0.0
>>> truncate_number(1.5)
0.0
>>> truncate_number(11.0)
0.0
``` 
This would confirm that the function indeed returns the decimal part of the input number.