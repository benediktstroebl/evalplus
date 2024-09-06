Here's the Python code that you asked for:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return number - int(number) // 1
    return number - int(number) // 1
```
This function takes a number as input and returns the decimal part of that number. It achieves this by first taking the number, then returning the integer part of the number (the largest integer smaller than the given number), and finally subtracting the integer part from the original number.