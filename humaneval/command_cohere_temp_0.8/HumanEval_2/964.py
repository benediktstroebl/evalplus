```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number itself. The decimals in the number will be subtracted, leaving only the integer part of the number if it is greater than 0. If the number is already an integer, the result will be 0, since the subtraction will result in a carry over of 1, meaning the whole number part gets added back to the result.