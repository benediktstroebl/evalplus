```python
def truncate_number(number: float) -> float:
    return number if number >= 1 else number // 10
```
The function checks if the number is greater than 1, and returns the floor division of the number by 10 if it is, and returns the original number if it's not.