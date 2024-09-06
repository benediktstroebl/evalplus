```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which leaves us with the leftover fraction (the decimal part of the original number). 

To better understand this, let's take a look at an example:
```python
print(truncate_number(3.5))  # Outputs: 0.5
```
In this example, the function subtracts the integer part of 3 (which is simply 3) from 3.5, leaving us with 0.5, which is the decimal part of 3.5. 

This function simply does the same thing every time, it always subtracts the largest integer part of the number and returns the leftover decimal part. 

Note: This function assumes that the input number is a positive decimal number. If the input number is a negative decimal number, the result will be negative too. If this is not the intended behavior for some cases, then you may want to add a check for the input number being positive before returning the truncated number.