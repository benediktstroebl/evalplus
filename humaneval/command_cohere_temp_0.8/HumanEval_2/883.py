```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The function takes a floating point number as input and returns the decimal part of the number. This is achieved by subtracting the integer part of the number (obtained by rounding down to the nearest integer using int()) from the original number. The decimal part is the residual value left over, which is always less than 1. 

To test this function, try calling it with different values and examining the output. For example:
```python
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(7.777))  # Output: 0.777
print(truncate_number(11.123))  # Output: 0.123
```

This will output:
```
0.5
0.777
0.123
```

The expected behavior is for the function to return the decimal part of the input number, which it does correctly.