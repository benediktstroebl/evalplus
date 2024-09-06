```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The function takes a floating point number as input and returns the decimal part of the number. This is achieved by subtracting the integer part of the number (obtained by converting the number to an integer) from the original number. The decimal part remaining in the result represents the portion of the original number that is less than 1. 

Here is an example usage of the function:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

The output of this code will be 0.5, confirming that the function correctly identifies the decimal part of the number as the residual after truncation to the nearest integer.