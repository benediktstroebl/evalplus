```python
def truncate_number(n: float) -> float:
    return n if not n.is_integer() else round(n // 10)
```

This function uses an if statement with the condition that checks if the number is not an integer. If the number is not an integer, it will return the number as is. Otherwise, the function will round the number to the integer part by dividing the number by 10.