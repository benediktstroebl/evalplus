```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which leaves us with the leftover fraction (the decimal part of the original number). 

To better understand this, let's take a look at an example: Let's say we have the number 3.5 and we run it through the `truncate_number` function. The largest integer that is less than 3.5 is 3. So we do the following calculation:
```
3.5 - 3 = 0.5
```
This result is the same as the decimals from the original number, so we've successfully isolated the decimal part. 

This method has a time complexity of O(1) since it only takes one step to obtain the decimal part. It is a straightforward and efficient solution suited for this problem.