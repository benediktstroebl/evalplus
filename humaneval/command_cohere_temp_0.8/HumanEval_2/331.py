```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which leaves us with the remaining fractional part of the number, which is what we want. 

To test this function, you can call it with any floating point number (let's call it number) and then verify that the output is equal to the fractional part of number, which can be computed as number - int(number).