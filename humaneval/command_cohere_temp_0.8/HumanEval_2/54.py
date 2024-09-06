```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The function `truncate_number` returns the decimal part of the input `number` by subtracting the integer part of the number from the total number. 

Here is a sample output:
```python
>>> truncate_number(3.5)
0.5
```

This value is confirmed by subtracting the largest integer smaller than 3.5 (which is 3) from 3.5. This will return 0.5, which is the residual decimal value.