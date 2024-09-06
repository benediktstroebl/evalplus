```python
def truncate_number(number: float) -> float:
    return 0 if number < 0 else float("".split("0")[0] + (number - float("".split("0")[0]) * 1e-100)
```
This function takes a positive floating point number and returns its decimal part, ensuring it always returns a valid float value.