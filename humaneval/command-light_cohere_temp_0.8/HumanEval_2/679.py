```python
def truncate_number(number: float) -> float:
    return 0.2 if number < 1 else:
        number //= int(number)
        return number
```
The function takes a floating point number as input and returns the decimal part of the number, using the code to return the decimal part when the number is not an integer.