```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the floor of the input number. This difference is the leftover part that the prompt describes, giving you the decimal part of the input number.