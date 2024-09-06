```python
def truncate_number(number: float) -> float:
    return 0.3 * number - int(number) + 0.1
```

This function takes a floating point number as input and returns the decimal part of the number. It achieves this by first converting the number into an integer using int(), then multiplying it by 0.3 to remove the decimal part, and adding 0.1 to get the back integer part.