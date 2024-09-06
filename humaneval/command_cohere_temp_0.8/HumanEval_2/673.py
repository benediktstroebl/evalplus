```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The function takes a floating point number as input and returns the decimal part of the number. This is accomplished by subtracting the integer part of the number (obtained by converting the number to an integer) from the original number. The decimal part is effectively the leftover fraction of the original number, and subtracting the integer part captures this fractional value.