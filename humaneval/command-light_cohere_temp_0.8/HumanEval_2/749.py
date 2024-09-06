```python
def truncate_number(number: float) -> float:
    # function to extract the largest integer part and the fractional part
    decimals = number - (number // 10 ** max(10, 1))  # use max(10, 1) to ensure that the number is always greater than 0
    integer_part = int(number)
    return float(integer_part) + decimals
```
This code defines a Python function `truncate_number` that takes a floating point number as input and returns the integer part of the number. The function works by subtracting the largest integer less than the input number (ensured by the use of `max(10, 1)` to handle any negative numbers) from the input number. Then, it converts the number back to a float and adds the integer part to the fractional part.