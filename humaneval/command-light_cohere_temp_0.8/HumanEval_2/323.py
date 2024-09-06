```python
def truncate_number(number: float) -> float:
    return max(number - n for n in range(int(number), 0, -1))
```
This function uses list comprehension and mathematical operations to find the largest integer less than the input number, which is the truncation of the number. It then returns the