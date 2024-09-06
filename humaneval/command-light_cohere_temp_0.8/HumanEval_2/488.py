```python
def truncate_number(number: float) -> float:
    return number - max(int(number), 0)
```

This function takes a number as an argument, and returns the decimal part of the number. It achieves this by subtracting the largest integer less than or equal to the number from it. This ensures that the maximum value is subtracted from the number, effectively removing the integer part.