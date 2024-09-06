Here's the function that solves the problem you described:
```python
def truncate_number(number: float) -> float:
    # Split the float number into the integer and decimal parts
    integer = number // 1
    decimal = number % 1

    # Return the decimal part
    return decimal
```

This function takes a floating point number as input and returns the decimal part of that number. It uses the `// 1` to get the integer part of the number and then calculates the remainder when dividing by 1 to get the decimal part.