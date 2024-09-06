```python
def truncate_number(number: float) -> float:
    # Use float precision to make sure the calculation works as expected
    return number - float('10' * int(number ** 0.2))
```
This function calculates the decimal part of a positive floating-point number by subtracting the product of 10 raised to the power of the integer part, and then returning the result as a float.