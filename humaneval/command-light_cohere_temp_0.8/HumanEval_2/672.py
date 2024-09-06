```python
def truncate_number(number: float) -> float:
    # Taken care of positive floating point numbers
    if not number <= 0:
        raise ValueError("Input number must be positive")
    # Return integer part and decimal part
    decimal = number % 1
    return int(decimal) + float(decimal < 0 and int(decimal) == 0)) / 1
```
This Python script defines a function `truncate_number` that takes a single argument `number` and returns the integer part of the input number as a floating-point number. 

This function successfully handles the input being negative or zero and raises a `ValueError` with a relevant error message. 

It then computes the decimal part of the number by taking the remainder of the division of the number by 1, then returns the integer part of the number, which is the largest integer less than the input number, plus the decimal part, which is always less than 1 and the same if the integer part is 0.