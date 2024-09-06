```python
def truncate_number(n: float) -> float:
    return 0 if n == 0 else int(n) if n > 0 else n
```
The function checks if the number is zero, and returns 0 in that case. If the number is greater than zero, the function uses int() function to remove the decimal part of a number. Then, it checks if the number is greater than zero, and returns the number itself.