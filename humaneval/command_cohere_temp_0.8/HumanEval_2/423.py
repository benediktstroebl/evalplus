```python
def truncate_number(number):
    return number - int(number)
```

The provided Python script defines a function `truncate_number` that takes a single argument, `number`, which is expected to be a positive floating-point number. The purpose of this function is to return the decimal part of the input number. This is achieved by subtracting the largest integer that is less than or equal to the input number from the input number itself. This operation effectively isolates the fractional part of the number, which is then returned as the result. 

The code employs a concise approach by utilizing the subtraction operation `int(number)` to isolate the decimal portion and skip the leftover part, which is always less than 1. This methodology demonstrates an elegant use of Python's built-in functionalities to simplify a problem involving decimal decomposition. 

This solution has a time complexity of O(1) since it involves a single arithmetic operation, making it an efficiently fast solution for isolating the decimal part of a floating-point number.