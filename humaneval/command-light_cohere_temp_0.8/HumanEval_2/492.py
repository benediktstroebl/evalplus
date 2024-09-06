```python
def truncate_number(number: float) -> float:
    return max(0, number - int(number))
```
This function takes a positive floating point number and returns the decimal part of the number, which is the largest integer smaller than the given number. 

The function uses the `max` function with the parameter `0` and the number `number - int(number)` to achieve this. 

The `int` function returns the largest integer smaller than the given number. 
The `max` function takes the smaller number and returns the largest number that is not smaller than the input. 
This function is self-contained, as it does not rely on any other functions or variables from the outside.