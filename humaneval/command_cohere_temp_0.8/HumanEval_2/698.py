```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The `truncate_number` function takes a floating point number as an input and returns the decimal part of the number by subtracting the integer part of the number. 

Here is an example usage of the function:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

This would return 0.5 as the output, which is the decimal part of the number 3.5. 

The code passes the given test case and returns the expected output of 0.5 when executing the function with the input 3.5. 

It's crucial to note, however, that the assumption here is that the given number has an integral part, which is greater than or equal to zero, and a fractional part that is less than or equal to 1. If these preconditions are not met, there may be unexpected behavior or the need for additional handling for negative numbers, large integers, or decimals larger than 1.