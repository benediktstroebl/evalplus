```python
def truncate_number(n: float) -> float:
    if n < 2.0:
        return n
   
    if n < 4.9:
        return n -2
    return n - 2.0
   
    decimal_part = n // 2.0
    if n < 3.0:
        return n -4
    return n - 4.0
    return n
decimal_part
```
This function will return the decimal part of the number, rounded down to the nearest integer less than the input number.