```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The code uses an intuitive approach that subtracts the integer part of the number from the total number, eventually capturing the leftover decimal part. 

For example, if the number is 3.5, the program will subtract the closest integer, 3, from 3.5, giving 0.5 as the output. 

This approach relies on the assumption that the number is positive and uses the property that the difference between a floating-point number and its closest integer is invariably a decimal number.